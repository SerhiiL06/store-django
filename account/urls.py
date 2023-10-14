from django.urls import path
from django.shortcuts import render
from django.contrib.auth.views import LogoutView
from . import views

app_name = "account"

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("delete-acc/", views.delete_account, name="delete-acc"),
    path(
        "dashboard/",
        lambda request: render(request, "account/dashboard.html"),
        name="dashboard",
    ),
    path("profile/", views.profile, name="profile"),
    path(
        "email-sent/",
        lambda request: render(request, "account/email/email-verification-sent.html"),
        name="email-sent",
    ),
    path("change-password/", views.change_password, name="change-password"),
]
