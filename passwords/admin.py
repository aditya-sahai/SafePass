from django.contrib import admin
from passwords.models import AppPassword, Key

admin.site.register(AppPassword)
admin.site.register(Key)
