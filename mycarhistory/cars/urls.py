from django.conf.urls.defaults import patterns, url
from mycarhistory.cars.views import CarMainView

urlpatterns = patterns('mycarhistory.cars.views',
                url(r'$', CarMainView.as_view(), name='cars_main'),)
