from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from shop.models import ProductProxy
from .cart import Cart


def cart_summary(request):
    cart = Cart(request)
    return render(request, "cart/cart-summary.html", {"cart": cart})


def cart_add(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        product_id = request.POST.get("product_id")
        product_qty = request.POST.get("product_qty")

        product = get_object_or_404(ProductProxy, id=product_id)

        cart.add(product=product, quantity=product_qty)

        cart_qty = cart.__len__()
        response = JsonResponse({"qty": cart_qty})
        return response


def cart_delete(request):
    pass


def cart_update(request):
    pass
