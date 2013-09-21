from django.db import models


class Mechanic(models.Model):

    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(default='', max_length=200)
    address = models.TextField(default='')
    email = models.EmailField(default='', max_length=254)
