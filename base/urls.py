from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django_email_verification import urls as email_urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("shop.urls"), name="shop"),
<<<<<<< HEAD
    path("email/", include(email_urls)),
    path("account/", include("account.urls")),
=======
    path("cart/", include("cart.urls"), name="cart"),
>>>>>>> cart
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
