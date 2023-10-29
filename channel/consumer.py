from channels.generic.websocket import WebsocketConsumer
import json
from django.contrib.auth import get_user_model
from product.models import CartProduct,Cart,Product
class WSConsumer(WebsocketConsumer):
    def connect(self):
        print("connect")
        self.accept()
    def disconnect(self, code):
        print("disconnect")
    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        type = data.get("type")
        user = data.get("user")
        product = None
        cart = None
        cart_product = None
        def send_count(cart,product,mode,card_product):
            count = 0
            for pack in cart.cart_products.all() :
                count += pack.count
            self.send(json.dumps({
                "slug" : product.slug,
                "mode" : mode,
                "price" : product.price,
                "count" : card_product.count,
                "total" : count,
            }))
        if user != "AnonymousUser":
            print('us')
            try :
                user = get_user_model().objects.get(mobile=user)
                print(user)
                try :
                    cart = user.carts.all().get(is_paid=False,is_open=True)
                except :
                    cart = Cart.objects.create(user=user)
                print(cart,"cart")
                try :
                    product = Product.objects.get(slug=data.get("slug"))
                except :
                    pass
                print(product,"product")
                try :
                    cart_product = cart.cart_products.all().get(product__slug=data.get("slug"))
                except :
                    cart_product = CartProduct.objects.create(cart=cart,product=product,count=0)
                print(cart_product)
            except :
                print("error")
        if type == "add-cart" :
            cart_product.count += 1
            cart_product.save()
            send_count(cart, product, "add",cart_product)
        if type == "remove-cart":
            if cart_product.count == 1 :
                cart_product.delete()
            else :
                cart_product.count -= 1
                cart_product.save()
                send_count(cart,product,"remove",cart_product)
        print(data)