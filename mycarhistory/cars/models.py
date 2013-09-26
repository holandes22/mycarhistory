import datetime
from django.db import models
from django.contrib.auth.models import User


YEAR_CHOICES = [(year, str(year)) for year in
                xrange(1920, datetime.datetime.now().year + 1)]


class Car(models.Model):

    GEARBOX_MANUAL = 1
    GEARBOX_AUTOMATIC = 2
    GEARBOX_CHOICES = (
        (GEARBOX_MANUAL, 'Manual'),
        (GEARBOX_AUTOMATIC, 'Automatic'),
    )

    user = models.ForeignKey(User)
    brand = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    year = models.IntegerField(
        choices=YEAR_CHOICES,
        default=str(datetime.datetime.now().year),
    )
    gearbox_type = models.IntegerField(
        choices=GEARBOX_CHOICES,
        default=GEARBOX_AUTOMATIC,
    )
    amount_of_owners = models.IntegerField(
        default=0,
        help_text='Amount of owners (incluing current)',
    )

    def is_automatic(self):
        return self.gearbox_type == self.GEARBOX_AUTOMATIC

    def get_full_name(self):
        return '{} {} {}'.format(self.brand, self.model, self.year)

    def __unicode__(self):
        return self.get_name()
