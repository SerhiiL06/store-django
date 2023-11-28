from django.shortcuts import render, redirect, HttpResponseRedirect
from cart.cart import Cart
from django.urls import reverse_lazy, reverse
from .forms import ShippingAddressForm
from shop.models import Product
from .models import ShippingAddress, Order, OrderItem
from django.views.generic import View, TemplateView
from django.http import JsonResponse
import stripe
from django.conf import settings
from base.settings import STRIPE_SECRET_KEY, STRIPE_VERSION
from decimal import Decimal


stripe.api_version = STRIPE_VERSION
stripe.api_key = STRIPE_SECRET_KEY


class ShippingAddressView(View):
    def get(self, request):
        profile, create = ShippingAddress.objects.get_or_create(user=request.user)

        form = ShippingAddressForm(instance=profile)

        return render(request, "payment/shipping.html", {"form": form})

    def post(self, request):
        profile = ShippingAddress.objects.get(user=request.user)

        form = ShippingAddressForm(request.POST, instance=profile)

        if form.is_valid():
            initial = form.save(commit=False)
            initial.user = request.user
            initial.save()

            return redirect("account:dashboard")

        return HttpResponseRedirect(request.META["HTTP_REFERER"])


class CheckoutView(View):
    def get(self, request):
        cart = Cart(request)
        for item in cart:
            print(item)
        if request.user.is_authenticated:
            ship_add, _ = ShippingAddress.objects.get_or_create(user=self.request.user)
            context = {"shipping_address": ship_add}
            return render(request, "payment/checkout.html", context)
        return render(request, "payment/checkout.html")


def order_complete(request):
    if request.method == "POST":
        email = request.POST["email"]
        full_name = request.POST["full_name"]
        city = request.POST["city"]
        street = request.POST["street"]
        zip_code = request.POST["zip_code"]

        user = request.user

        ship_address, _ = ShippingAddress.objects.get_or_create(
            user=user,
            defaults={
                "email": email,
                "full_name": full_name,
                "city": city,
                "street": street,
                "zip_code": zip_code,
            },
        )

        cart = Cart(request)

        total_price = cart.get_total_price()

        order = Order.objects.create(
            shipping_address=ship_address, total_price=total_price
        )

        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item["product"],
                quantity=item["qty"],
                price=item["price"],
            )

            session = stripe.checkout.Session.create(
                mode="payment",
                success_url=request.build_absolute_uri(
                    reverse("payment:payment-success")
                ),
                cancel_url=request.build_absolute_uri(
                    reverse("payment:payment-failed")
                ),
                line_items=[
                    (
                        {
                            "price_data": {
                                "unit_amount": int(item["price"] * Decimal(100)),
                                "currency": "uah",
                                "product_data": {"name": item["product"]},
                            },
                            "quantity": item["qty"],
                        }
                    )
                ],
            )

        print("Before redirect")  # Добавьте эту строку

        return redirect(session.url)


class PaymentSuccessView(TemplateView):
    template_name = "payment/payment-success.html"


class PaymentFailedView(TemplateView):
    template_name = "payment/payment-failed.html"
