if __name__ == "__main__":
    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SafePass.settings")

    import django
    django.setup()

from django.contrib.auth.models import User
from passwords.models import AppPassword, Key

from cryptography.fernet import Fernet


class PasswordManager:
    def __init__(self, user):
        self.USER = user

        # if key:
        #     self.KEY = key.decode()
        # else:
        #     self.KEY = Fernet.generate_key()

    def save_new_password(self, app, password):
        """
        Saves password and key in db.
        """

        key = Fernet.generate_key()
        cryptor = Fernet(key)

        encrypted_password = cryptor.encrypt(password.encode()).decode()
        # encrypted_app = self.cryptor.encrypt(app.encode()).decode()

        ap = AppPassword(user=self.USER, app=app, password=encrypted_password)
        k = Key(password=ap, key=key.decode())

        ap.save()
        k.save()

    def decrypt_saved_data(self, app):
        """
        Gets ecrypts the encrypted password and app
        """

        saved_pass = AppPassword.objects.get(user=self.USER, app=app)

        if saved_pass:
            key = Key.objects.get(password=saved_pass).key
            cryptor = Fernet(key.encode())
            decrypted_password = cryptor.decrypt(saved_pass.password.encode()).decode()
            return decrypted_password

        else:
            return False


if __name__ == "__main__":
    a = User.objects.get(username="aditya")
    Manager = PasswordManager(a)

    app = input("Enter name of app: ")
    # password = input(f"Enter password for {app}: ")

    # Manager.save_new_password(app, password)
    Manager.decrypt_saved_data(app)