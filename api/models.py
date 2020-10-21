from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Genre(models.Model):
    name = models.CharField()
    slug = models.SlugField(unique=True)


class Catigories(models.Model):
    name = models.CharField()
    slug = models.SlugField(unique=True)


class Title(models.Model):
    name = models.CharField()
    year = models.IntegerField()
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=PROTECT , related_name='title')
    category = models.ForeignKey(Categories, on_delete=PROTECT , related_name='catigories')
