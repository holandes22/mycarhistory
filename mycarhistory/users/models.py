from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    full_name = models.CharField(max_length=150, default='')
    short_name = models.CharField(max_length=50, default='',
            help_text='How would you like to be addressed?')

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.short_name
