from django.shortcuts import render, redirect
from passwords.models import AppPassword, Key
from passwords.utils.PasswordManager import PasswordManager
from django.contrib.auth.decorators import login_required


@login_required()
def view_passwords(request):

    if request.method == "POST":
        action = request.POST.get("action")
        app = action.split(":")[1].strip()

        if action.split(":")[0] == "delete":
            AppPassword.objects.get(app=app).delete()

        else:
            Manager = PasswordManager(request.user)
            password = Manager.decrypt_saved_data(app)
            return redirect(f"/passwords/edit-password/{app}/")

    user = request.user
    user_passwords = AppPassword.objects.filter(user=user)

    app_passwords = []
    Manager = PasswordManager(user)

    for i, Password in enumerate(user_passwords):
        password = Manager.decrypt_saved_data(Password.app)
        # print(Password.app, password)
        app_passwords.append(
            {
                "num": i + 1,
                "app": Password.app,
                "password": password
            }
        )
    return render(request, "passwords/view_passwords.html", context={"app_passwords": app_passwords})

@login_required()
def new_password(request):
    return render(request, "passwords/new_password.html")

@login_required()
def edit_password(request, app):
    Manager = PasswordManager(request.user)

    if request.method == "POST":
        app_password = AppPassword.objects.get(app=app)
        app_password.app = request.POST.get("app")
        key = Key.objects.get(password=app_password).key
        app_password.password = Manager.encrpyt_password(request.POST.get("password"), key)
        app_password.save()

        return redirect("/passwords/view-passwords/")

    else:
        password = Manager.decrypt_saved_data(app)

    return render(request, "passwords/edit_password.html", {"app": app, "password": password})