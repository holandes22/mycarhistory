from django.db import models
from django.contrib.auth.models import User
from mycarhistory.countries import CountryField
from mycarhistory.basemodel import BaseModel
from django.db.models import permalink

class Mechanic(BaseModel):

    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    telephone = models.CharField(max_length=25)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    country = CountryField()
    email = models.EmailField(blank=True)
    specialization = models.CharField(max_length=100, default='General', help_text='Comma separated if several, e.g: bodywork, A/C')

    def __unicode__(self):
        return "%s %s" % (self.name, self.lastname)

    @permalink
    def get_absolute_url(self):
        return ('mechanic-detail', (), {'pk': self.pk})


