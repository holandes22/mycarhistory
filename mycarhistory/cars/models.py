import datetime

from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db.models import permalink

from mycarhistory.basemodel import BaseModel
from mycarhistory.mechanics.models import Mechanic

DATE_FORMAT = '%m/%d/%Y'

def make_custom_field_callback(field):
    """
    Callback to make field customization. This is useful to midifiy the elements of a form, for example
    a custom class to a date field so it can be identified by Jquery UI datepicker in the template
    """
    formfield = field.formfield()
    if formfield:
        formfield.widget.attrs.update({'title': field.help_text})
    if isinstance(field, models.DateField):
        formfield.widget.format = DATE_FORMAT
        formfield.widget.attrs.update({'class':'datePicker', 'readonly':'true'})
    return formfield

class Car(BaseModel):

    SEDAN_TYPE = 1
    HATCHBACK_TYPE = 2
    COUPE_TYPE = 3
    WAGON_TYPE = 4
    SPORT_TYPE = 5
    TYPE_CHOICES = (
                  (SEDAN_TYPE, 'Sedan'),
                  (HATCHBACK_TYPE, 'Hatchback'),
                  (COUPE_TYPE, 'Coupe'),
                  (WAGON_TYPE, 'Station wagon'),
                  (SPORT_TYPE, 'Sport'),
                  )

    YEARS = [year for year in xrange(1920, datetime.datetime.now().year + 1)]
    YEAR_CHOICES = zip(YEARS, map(lambda x: str(x), YEARS))

    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    user = models.ForeignKey(User)
    car_type = models.IntegerField(choices=TYPE_CHOICES, default=SEDAN_TYPE)
    is_automatic = models.BooleanField(default=True)
    gears = models.IntegerField(default=5)
    hand = models.IntegerField(default=0, help_text='Number of previous owners when purchased')
    year = models.IntegerField(choices=YEAR_CHOICES, default=str(datetime.datetime.now().year))
    purchase_date = models.DateField(default=datetime.datetime.now, help_text='Purchase date')
    kilometrage_when_purchased = models.IntegerField(help_text='Kilometrage when purchased')
    color = models.CharField(max_length=100)

    def __unicode__(self):
        return '%s %s %s' % (self.brand, self.model, self.year)

    def was_new_when_bought(self):
        return self.hand == 0

    @permalink
    def get_absolute_url(self):
        return ('car-detail', (), {'pk': self.pk})

class CarForm(ModelForm):
    formfield_callback = make_custom_field_callback
    class Meta:
        model = Car
        readonly_fields = ['user']
        exclude = ['user']


class TreatmentEntry(BaseModel):


    BODYWORK_CAT = 1
    ELECTRIC_CAT = 2
    ENGINE_CAT = 3
    WHEELS_CAT = 4
    CHASIS_CAT = 5
    TREATMENT_CATS = (
                      (BODYWORK_CAT, 'Body work'),
                      (ELECTRIC_CAT, 'Electricity'),
                      (ENGINE_CAT, 'Engine'),
                      (WHEELS_CAT, 'Wheels'),
                      (CHASIS_CAT, 'Chasis'),
                      )

    BROKEN_REASON = 1
    SERVICE_REASON = 2
    AESTHETIC_REASON = 3
    NO_REASON = 4
    TREATMENT_REASONS = (
                         (BROKEN_REASON, 'Failing component'),
                         (SERVICE_REASON, 'Service'),
                         (AESTHETIC_REASON, 'Aesthetic'),
                         (NO_REASON, 'No reason'),
                         )

    car = models.ForeignKey(Car)
    mechanic = models.ForeignKey(Mechanic)
    reason = models.IntegerField(choices=TREATMENT_REASONS, default=BROKEN_REASON)
    description = models.TextField()
    category = models.IntegerField(choices=TREATMENT_CATS, default=BODYWORK_CAT)

    class Meta:
        abstract = True

    def __unicode__(self):
        return '%s %s' % (self.formatted_date(), self.car)

    def formatted_date(self):
        return self.date.strftime('%b/%d/%Y')

class CarTreatmentEntry(TreatmentEntry):

    date = models.DateField(default=datetime.datetime.now)
    parts_replaced = models.CharField(max_length=300, default='None',
                                      help_text='Replaced parts during treatment, comma separated')
    kilometrage = models.IntegerField(help_text='Kilometrage at the moment of the treatment')
    cost = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Car treatment entries'


class PlannedCarTreatmentEntry(TreatmentEntry):

    planned = models.BooleanField(default=False)
    kilometrage = models.IntegerField(help_text='The planned kilometrage to take the car to the mechanic')
    date = models.DateField(default=datetime.datetime.now,
                            help_text='The planned date to take the car for treatment')
    notify = models.BooleanField(default=False, help_text='Would you like to receive a reminder')
    notify_date = models.DateField()
    notify_method = models.TextField()

    class Meta:
        verbose_name_plural = 'Planned cat treatment entries'
