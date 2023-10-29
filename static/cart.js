let websocket ;
const totalPrice = $("#total_price");
const startWebSocket = ()=>{
    websocket = new WebSocket(`ws://${window.location.host}/ws/cart/`);
}
startWebSocket();
websocket.onerror = ()=> {
    console.log("error in connecting")
    setInterval(()=>{
        console.log("trying to connect ...");
        startWebSocket();
    },2000)
}
websocket.onmessage = (e)=>{
    data = JSON.parse(e.data)
    let productTotalPrice = $(`.total-price-${data.slug}`);
    let productCount = $(`.count-${data.slug}`)
    if(data.mode == "add"){
        productCount.text(data.count)
        productTotalPrice.text(data.price * data.count)
    }if(data.mode == "remove"){
        productCount.text(data.count)
        productTotalPrice.text(data.price * data.count)
    }if(data.mode == "delete"){
        alert(data.mode)
        $(`#product-${data.slug}`).addClass("hide")
    }
}
function btnAddCart(slug,user){
    websocket.send(JSON.stringify({
        "slug" : slug,
        "type" : "add-cart",
        "user" : user
    }));
    Swal.fire({
        "title" : "افزایش یافت",
        "icon" :"success"
    })
};
function btnRemoveCart(slug,user){
    websocket.send(JSON.stringify({
        "type" : "remove-cart",
        "user" : user ,
        "slug" : slug
    }));
    Swal.fire({
        "title" : "کاهش یافت",
        "icon" :"success",
    })
};