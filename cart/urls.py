from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("", views.cart_summary, name="cart"),
    path("add/", views.cart_add, name="add_to_cart"),
]
