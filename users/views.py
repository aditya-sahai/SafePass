from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from users.forms import SignUpForm, ChangePasswordForm
from django.contrib.auth.decorators import login_required
from users.utils.authenticate import check_pw, add_pepper


def index(request):
    return render(request, "index.html")

def user_login(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = check_pw(password, username)

        if user:
            login(request, user)
            return redirect("/")

        else:
            credentials_are_valid = False

    else:
        credentials_are_valid = True

    return render(request, "users/user_login.html", {"credentials_are_valid": credentials_are_valid})

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

            Sender = EmailSender(user)
            Sender.send_new_user_mail()

            user.set_password(add_pepper(user.password))
            user.save()


            login(request, user)

            return redirect("/")

    else:
        signup_form = SignUpForm()

    return render(request, "users/user_signup.html", {"form": signup_form})

@login_required()
def change_password(request):

    password_changed = False

    if request.method == "POST":

        change_password_form = ChangePasswordForm(request.POST)
        user = request.user

        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_new_password")

        if new_password != confirm_password:
            change_password_form.add_error("new_password", "Passwords do not match.")

        # print(user.check_password(old_password))

        if not user.check_password(old_password):
            change_password_form.add_error("old_password", "Invalid Password.")

        if change_password_form.is_valid():
            user.set_password(add_pepper(new_password))
            user.save()
            login(request, user)
            password_changed = True
            change_password_form = ChangePasswordForm()

    else:
        change_password_form = ChangePasswordForm()

    return render(request, "users/change_password.html", {
            "form": change_password_form,
            "password_changed": password_changed,
        }
    )