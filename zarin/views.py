from django.conf import settings
import requests
from django.shortcuts import redirect
import json
from django.contrib.messages import success,error
if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'

ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
phone = 'YOUR_PHONE_NUMBER'  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://127.0.0.1:8000/zarin/verify/'


def request_payment(request):
    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": request.user.carts.filter(is_paid=False,is_open=True).first().get_total_price(),
        "Description": description,
        "CallbackURL": CallbackURL,
    }
    print(request.user.carts.filter(is_paid=False,is_open=True).first().get_total_price())
    cart = request.user.carts.filter(is_open=True, is_paid=False).first()
    data["Amount"] = request.user.carts.filter(is_paid=False,is_open=True).first().get_total_price()
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data))}
    try:
        response = requests.post(ZP_API_REQUEST, data=data, headers=headers, timeout=10)
        print(response.status_code)
        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                return redirect(ZP_API_STARTPAY + str(response['Authority']))
            else:
                error(request,"مشکلی در پرداخت پیش امده")
                return redirect("product:cart")
        return JsonResponse(response)

    except requests.exceptions.Timeout:
        return JsonResponse({'status': False, 'code': 'timeout'})
    except requests.exceptions.ConnectionError:
        return JsonResponse({'status': False, 'code': 'connection error'})


def verify(request):
    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": request.user.carts.filter(is_paid=False,is_open=True).first().get_total_price(),
        "Authority": request.GET.get("Authority"),
    }
    cart = request.user.carts.filter(is_open=True,is_paid=False).first()
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data))}
    response = requests.post(ZP_API_VERIFY, data=data, headers=headers)
    if response.status_code == 200:
        response = response.json()
        if response['Status'] == 100:
            for cart_product in cart.cart_products.all():
                cart_product.product.count_buy += 1
                cart_product.product.save()
            cart.is_paid = True
            cart.is_open= False
            cart.save()
            success(request,"پرداخت شما با موفقیت انجام شد ")
            return redirect("product:main")
        else:
            error(request,"خطایی رخ داد ")
            return redirect("product:main")
    return response