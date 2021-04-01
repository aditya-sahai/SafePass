from django import forms
from passwords.models import AppPassword


class AppPasswordForm(forms.Form):
    app = forms.CharField(max_length=120)
    password = forms.CharField(max_length=120)