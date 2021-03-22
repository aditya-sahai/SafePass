from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def user_login(request):
    return render(request, "users/user_login.html")

def user_logout(request):
    return render(request, "users/user_logout.html")

def user_signup(request):
    return render(request, "users/user_signup.html")
