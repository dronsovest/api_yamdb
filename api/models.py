import datetime

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
    name = models.CharField(max_length=60,
                            verbose_name='название произведения')
    year = models.IntegerField(verbose_name='год опубликования', null=True,
                               blank=True, )
    description = models.TextField(verbose_name='описание')
    genre = models.ManyToManyField(Genre, related_name="title",
                                   verbose_name='жанр')
    category = models.ForeignKey(Catigories, on_delete=models.SET_NULL,
                                 null=True, related_name="category")
