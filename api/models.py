from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Genre(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(unique=True)


class Catigories(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(unique=True)


class Title(models.Model):
    name = models.CharField(max_length=60)
    year = models.IntegerField()
    description = models.TextField()
    genre = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,
        related_name="title"
    )
    category = models.ForeignKey(
        Catigories,
        on_delete=models.PROTECT,
        related_name="catigory"
    )
