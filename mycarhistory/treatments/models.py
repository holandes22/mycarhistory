import datetime
from django.db import models

from mycarhistory.cars.models import Car


class Treatment(models.Model):

    BODYWORK_CAT = 'bodywork'
    ELECTRIC_CAT = 'electricity'
    ENGINE_CAT = 'engine'
    WHEELS_CAT = 'wheels'
    CHASSIS_CAT = 'chassis'
    TREATMENT_CATS = (
        (BODYWORK_CAT, 'Body work'),
        (ELECTRIC_CAT, 'Electricity'),
        (ENGINE_CAT, 'Engine'),
        (WHEELS_CAT, 'Wheels'),
        (CHASSIS_CAT, 'Chassis'),
    )

    BROKEN_REASON = 'broken'
    SERVICE_REASON = 'service'
    AESTHETIC_REASON = 'aesthetic'
    NO_REASON = 'none'
    TREATMENT_REASONS = (
        (BROKEN_REASON, 'Failing component'),
        (SERVICE_REASON, 'Service'),
        (AESTHETIC_REASON, 'Aesthetic'),
        (NO_REASON, 'No reason'),
    )

    car = models.ForeignKey(Car, related_name='treatments')
    done_by = models.CharField(default='', max_length=150)
    description = models.TextField(blank=True)
    date = models.DateField(
        default=datetime.datetime.now(),
        # TODO: just for now until fixed date serialize at frontend:
        # https://github.com/toranb/ember-data-django-rest-adapter/issues/61
        # put back as mandatory afterwards
        blank=True,
        null=True,
    )
    kilometrage = models.IntegerField(help_text='Kilometrage at the time')
    reason = models.CharField(
        max_length=50,
        choices=TREATMENT_REASONS,
        default=NO_REASON,
    )
    category = models.CharField(
        max_length=50,
        choices=TREATMENT_CATS,
        default=BODYWORK_CAT,
    )
    parts_replaced = models.CharField(
        max_length=400,
        blank=True,
        help_text='Replaced parts, comma separated',
    )
