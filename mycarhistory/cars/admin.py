from django.contrib import admin
from mycarhistory.cars.models import Car, CarTreatmentEntry, PlannedCarTreatmentEntry

admin.site.register(Car)
admin.site.register(CarTreatmentEntry)
admin.site.register(PlannedCarTreatmentEntry)
