from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UserChangeForm,
    PasswordChangeForm,
)
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254, label="Your email", widget=forms.EmailInput, required=True
    )
    username = forms.CharField(help_text="")
    password1 = forms.CharField(
        widget=forms.PasswordInput(),
        help_text="Your password can't be too similar to your other personal information.",
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ["username", "password"]


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(), required=True)
    email = forms.EmailField(widget=forms.EmailInput(), required=True)

    class Meta:
        model = User
        fields = ["username", "email"]


class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ["old_password", "new_password1", "new_password2"]
