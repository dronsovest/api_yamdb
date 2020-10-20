from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class UserRole(models.TextChoices):
        USER = "user"
        MODERATOR = "moderator"
        ADMIN = "admin"

    role = models.CharField(
        choices=UserRole.choices,
        default=UserRole.USER,
        max_length=20,
        verbose_name="Роль",
    )
    bio = models.TextField(max_length=1000, blank=True,
                           verbose_name="О себе", )

    def __str__(self):
        full_name = self.get_full_name()
        return f"{self.role}: {full_name}"
