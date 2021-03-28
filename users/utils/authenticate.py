if __name__ == "__main__":
    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SafePass.settings")

    import django
    django.setup()

from django.contrib.auth import authenticate

import random
import string


def check_pw(raw_password, username):
    for pepper in string.ascii_uppercase + string.ascii_lowercase:
        user = authenticate(username=username, password=raw_password + pepper)

        if user:
            return user

    return False

def add_pepper(raw_password):
    password = raw_password + random.choice(string.ascii_uppercase + string.ascii_lowercase)
    return password

if __name__ == "__main__":
    peppered_password = add_pepper("Aytida$123")
    print(peppered_password)

    user = check_pw("Aytida$123", "aditya")
    print(user)