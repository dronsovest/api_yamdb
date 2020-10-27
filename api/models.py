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
    genre = models.ManyToManyField(
        Genre,
        related_name="title"
    )
    category = models.ForeignKey(
        Catigories,
        on_delete=models.SET_NULL,
        null=True,
        related_name="catigory"
    )


class Review(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name="reviewer"
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name="title"
    )
    text = models.TextField(max_length=1000)
    score = models.IntegerField(null=False)
    pub_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)
