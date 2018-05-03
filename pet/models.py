from django.db import models

# Create your models here.

class Pet(models.Model):
    '''Implements pet model'''
    name = models.CharField(max_length=20)
    race = models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    owner = models.CharField(max_length=20)

    def __str__(self):
        return self.name
