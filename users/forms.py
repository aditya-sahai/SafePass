from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
import string


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label="Password", validators=[validate_password])
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    username = forms.CharField(label="Username")
    email = forms.EmailField(label="Email Address")

    class Meta:
        model = User
        fields = ("username", "email", "password")

    def clean_email(self):
        user_email = self.cleaned_data["email"]
        users = list(User.objects.raw(f"SELECT * FROM auth_user where email='{user_email}';"))

        if users != []:
            raise ValidationError("User with that email already exists.")

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(), label="Old Password")
    new_password = forms.CharField(widget=forms.PasswordInput(), label="New Password", validators=[validate_password])
    confirm_new_password = forms.CharField(widget=forms.PasswordInput(), label="Confirm New Password")

    # def clean_new_password(self):
    #     new_password = self.cleaned_data["new_password"]
    #     contains_digit = False

    #     for digit in string.digits:
    #         if digit in new_password:
    #             contains_digit = True

    #     if new_password.lower() == new_password:
    #         self.add_error("new_password", "Password must contain at least 1 uppercase character.")

    #     if not contains_digit:
    #         self.add_error("new_password", "Password must contain at least 1 number.")

    #     return new_password