from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .forms import RegisterForm, LoginForm, UserProfileForm, ChangePasswordForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from django.contrib.auth import login, authenticate


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")

            user = User.objects.create_user(
                email=email, username=username, password=password
            )

            user.is_active = False

            return redirect("account:email-sent")

    form = RegisterForm()
    return render(request, "account/register.html", {"form": form})


def login_view(request):
    form = LoginForm()

    # if request.user.is_auntheticated:
    #     return redirect("shop:products")

    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "You're login!")
            return redirect("shop:products")

    return render(request, "account/login.html", {"form": form})


def profile(request):
    form = UserProfileForm(instance=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(request.META["HTTP_REFERER"])

    return render(request, "account/profile-management.html", {"form": form})


def delete_account(request):
    user = User.objects.get(id=request.user.id)
    user.delete()
    messages.success(request, "You delete you account!")
    return redirect("shop:products")


def change_password(request):
    form = ChangePasswordForm(user=request.user)

    if request.method == "POST":
        form = ChangePasswordForm(user=request.user)
        old_passoword = request.POST.get("old_password")
        new_password = request.POST.get("new_password2")
        user = request.user
        if user.check_password(old_passoword):
            user.set_password(new_password)
            user.save()
            messages.success(request, "Your password was edit")
            return redirect("account:login")
        else:
            messages.error(request, "Please try again!")
            return HttpResponseRedirect(request.META["HTTP_REFERER"])

    return render(request, "account/change-password.html", {"form": form})
