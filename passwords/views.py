from django.shortcuts import render


def view_passwords(request):
    return render(request, "passwords/view_passwords.html")

def manage_passwords(request):
    return render(request, "passwords/manage_passwords.html")