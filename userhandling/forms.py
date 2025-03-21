from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.utils.translation import gettext_lazy as _

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label=_("E-mail"), max_length=254)
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
