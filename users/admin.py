from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'confirmation_code',)


admin.site.register(CustomUser, CustomUserAdmin)
