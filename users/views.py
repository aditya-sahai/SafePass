from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from users.forms import SignUpForm


def index(request):
    return render(request, "index.html")

def user_login(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("/")

    return render(request, "users/user_login.html")

def user_logout(request):
    logout(request)
    return redirect("/")

def user_signup(request):

    if request.method == "POST":
        signup_form = SignUpForm(data=request.POST)

        if request.POST.get("password") != request.POST.get("confirm_password"):
            signup_form.add_error("password", "Passwords do not match.")

        if signup_form.is_valid():

            user = signup_form.save()
            print(user.email)
            user.set_password(user.password)
            user.save()

            login(request, user)

            return redirect("/")

    else:
        signup_form = SignUpForm()

    return render(request, "users/user_signup.html", {"form": signup_form})
