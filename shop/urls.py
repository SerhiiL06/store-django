from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path("", views.product_view, name="products"),
    path("product/<slug:slug>/", views.product_detail, name="detail"),
    path("category/<slug:slug>/", views.category_list, name="category"),
]
