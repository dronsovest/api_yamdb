from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import CustomUser as User


class Category(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(unique=True)
    
    
class Genre(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(unique=True)


class Title(models.Model):
    name = models.CharField(max_length=60)
    year = models.IntegerField()
    description = models.TextField()
    genre = models.ManyToManyField(Genre, related_name="title")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name="Category",
    )

    class Meta:
        ordering = ["id"]


class Review(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviewer",
        null=False
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name="title",
        null=False,
    )
    text = models.TextField(max_length=1000)
    score = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)], null=False,
    )
    pub_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    class Meta:
        ordering = ["id"]


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="commenter"
    )
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name="review"
    )
    text = models.TextField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    class Meta:
        ordering = ["id"]
