from django.db import models


class Car(models.Model):

    brand = models.TextField(max_length=100)
    name = models.TextField(max_length=100)
    year = models.IntegerField()

