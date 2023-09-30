from django.test import TestCase
from django.urls import reverse
from .models import Product, ProductProxy, Category
from http import HTTPStatus


class ProductViewTestCase(TestCase):
    def test_get_products(self):
        path = reverse("shop:products")
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "shop/products.html")
