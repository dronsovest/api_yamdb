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
    bio = models.TextField(
        max_length=1000, blank=True, null=True, verbose_name="О себе",
    )

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.role}: {self.email}"
