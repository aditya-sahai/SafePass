from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label="Password", validators=[validate_password])
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    username = forms.CharField(label="Username")
    email = forms.EmailField(label="Email Address")

    class Meta:
        model = User
        fields = ("username","email","password")

    # def clean(self):
    #     cleaned_data = super(UserForm, self).clean()
    #     password = cleaned_data.get("password")
    #     confirm_password = cleaned_data.get("confirm_password")

    #     # print(f"{password}{confirm_password}")

    #     if password != confirm_password:
    #         self.add_error("password", "Passwords do not match.")
