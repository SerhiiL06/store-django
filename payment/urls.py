from django.urls import path
from django.shortcuts import render
from . import views
from django.contrib.auth.decorators import login_required


app_name = "payment"

urlpatterns = [
    path(
        "shipping/",
        login_required(views.ShippingAddressView.as_view()),
        name="shipping",
    ),
    path("checkout/", views.CheckoutView.as_view(), name="checkout"),
    path("complete-order/", views.order_complete, name="complete-order"),
    path("payment-success", views.PaymentSuccessView.as_view(), name="payment-success"),
    path("payment-failed", views.PaymentFailedView.as_view(), name="payment-failed"),
]
