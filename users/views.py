from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from users.forms import UserForm


def index(request):
    return render(request, "index.html")

def user_login(request):
    return render(request, "users/user_login.html")

def user_logout(request):
    logout(request)
    return redirect("/")

def user_signup(request):

    if request.method == "POST":
        signup_form = UserForm(data=request.POST)
        # print()
        # print(signup_form.is_valid())
        # print(signup_form._errors)
        # print()
        if request.POST.get("password") != request.POST.get("confirm_password"):
            signup_form.add_error("password", "Passwords do not match.")

        if signup_form.is_valid():
                user = signup_form.save()
                user.set_password(user.password)
                user.save()

                login(request, user)

                return redirect("/")

    else:
        signup_form = UserForm()

    return render(request, "users/user_signup.html", {"form": signup_form})
