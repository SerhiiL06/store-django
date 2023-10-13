from django.contrib import admin
from .models import Category, Product, ProductProxy


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "parent", "slug"]
    ordering = ["name"]

    def get_prepopulated_fields(self, request, obj=None):
        return {
            "slug": ("name",),
        }


@admin.register(ProductProxy)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "price"]

    def get_prepopulated_fields(self, request, obj=None):
        return {
            "slug": ("title",),
        }
