from django.db import models
from django.core.validators import (
    MaxValueValidator,
    MinLengthValidator,
    MinValueValidator,
)
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=20, validators=[MinLengthValidator(2)])

    def __str__(self) -> str:
        return self.name


class ISBN(models.Model):
    number = models.BigAutoField(primary_key=True)
    book = models.OneToOneField("Book", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.number}"


class Book(models.Model):
    desc = models.CharField(max_length=1000)
    title = models.CharField(max_length=50, validators=[MinLengthValidator(10)])
    rate = models.FloatField(validators=[MaxValueValidator(5), MinValueValidator(0)])
    views = models.IntegerField(validators=[MinValueValidator(0)])
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    # isbn = models.OneToOneField(ISBN, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
