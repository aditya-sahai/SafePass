from django.db import models
from django.contrib.auth.models import User


class AppPassword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app = models.CharField(max_length=120)
    password = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.user.username}: {self.app}"

class Key(models.Model):
    password = models.OneToOneField(AppPassword, on_delete=models.CASCADE)
    key = models.CharField(max_length=44)

    def __str__(self):
        return str(self.password)