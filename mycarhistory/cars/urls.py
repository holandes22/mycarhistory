from django.conf.urls.defaults import patterns, url
from mycarhistory.cars.views import CarMainView, CarDetailView, CarCreateView


urlpatterns = patterns('mycarhistory.cars.views',
                url(r'main/$', CarMainView.as_view(), name='cars-main'),
                url(r'car/(?P<pk>\d+)/details/$', CarDetailView.as_view(), name='car-detail'),
                url(r'car/create/$', CarCreateView.as_view(), name='car-create'),
                )
