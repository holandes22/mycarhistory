from django.conf.urls.defaults import patterns, url
from mycarhistory.cars.views import CarMainView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView
from mycarhistory.cars.views import CarListView
from mycarhistory.cars.views import CarTreatmentCreateView, CarTreatmentListView


urlpatterns = patterns('mycarhistory.cars.views',
    url(r'main/$', CarMainView.as_view(), name='cars-main'),
    url(r'car/list/$', CarListView.as_view(), name='car-list'),
    url(r'car/(?P<pk>\d+)/details/$', CarDetailView.as_view(), name='car-details'),
    url(r'car/create/$', CarCreateView.as_view(), name='car-create'),
    url(r'car/(?P<pk>\d+)/update/$', CarUpdateView.as_view(), name='car-update'),
    url(r'car/(?P<pk>\d+)/delete/$', CarDeleteView.as_view(), name='car-delete'),
    # Treatments
    url(r'car/treatment/create/$', CarTreatmentCreateView.as_view(), name='cartreatmententry-create'),
    url(r'car/(?P<car_pk>\d+)/treatment/list/$', CarTreatmentListView.as_view(), name='car-treatment-list'),
    )
