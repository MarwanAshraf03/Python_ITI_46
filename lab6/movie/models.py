from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.TextField(max_length=15)
    description = models.TextField(max_length=100)
    release_date = models.DateField()
    categories = models.ManyToManyField("Category")
    casts = models.ManyToManyField("Cast")
    poster_image = models.ImageField()

    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    name = models.TextField(max_length=20)

    def __str__(self) -> str:
        return self.name


class Cast(models.Model):
    name = models.TextField(max_length=20)

    def __str__(self) -> str:
        return self.name
