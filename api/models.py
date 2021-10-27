from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
class Breed(models.Model):
    TINY = 'Tiny'
    SMALL = 'Small'
    MEDIUM = 'Medium'
    LARGE = 'Large'
    SIZE_CHOICES = (
        (TINY, 'Tiny'),
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large')
    )
    name = models.CharField(max_length=200)
    size = models.CharField(max_length=6, choices=SIZE_CHOICES, default=MEDIUM)
    friendliness= models.IntegerField(default=1, validators=[ MaxValueValidator(5), MinValueValidator(1) ])
    trainability= models.IntegerField(default=1, validators=[ MaxValueValidator(5), MinValueValidator(1) ])
    sheddingamount= models.IntegerField(default=1, validators=[ MaxValueValidator(5), MinValueValidator(1) ])
    exerciseneeds= models.IntegerField(default=1, validators=[ MaxValueValidator(5), MinValueValidator(1) ])


class Dog(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    favoritefood = models.CharField(max_length=200)
    favoritetoy = models.CharField(max_length=200)