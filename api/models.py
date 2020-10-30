from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import CustomUser as User


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
    genre = models.ManyToManyField(Genre, related_name="title")
    category = models.ForeignKey(
        Catigories,
        on_delete=models.SET_NULL,
        null=True,
        related_name="catigory",  # FIXME
    )

    class Meta:
        ordering = ["id"]


class Review(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviewer",  # FIXME
        null=False,
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name="title",  # FIXME
        null=False,
    )
    text = models.TextField(max_length=1000)
    score = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)], null=False,
    )
    pub_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    class Meta:
        ordering = ["id"]


class Comments(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="commenter"
    )
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name="review"  # FIXME
    )
    text = models.TextField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    class Meta:
        ordering = ["id"]
