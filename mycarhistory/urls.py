from django.contrib import admin
from django.conf import settings
from django.conf.urls import patterns, include, url

from mycarhistory.views import HomePageView, BrowserIDPageView
from mycarhistory.cars.views import CarListAPIView, CarDetailAPIView
from mycarhistory.treatments.views import TreatmentListByCarAPIView
from mycarhistory.treatments.views import TreatmentDetailByCarAPIView
from mycarhistory.treatments.views import TreatmentListAPIView
from mycarhistory.treatments.views import TreatmentDetailAPIView


admin.autodiscover()

urlpatterns = patterns(
    'mycarhistory',
    # API
    url(
        r'^api/v1/cars/$',
        CarListAPIView.as_view(),
        name='car-list',
    ),
    url(
        r'^api/v1/cars/(?P<pk>\d+)/$',
        CarDetailAPIView.as_view(),
        name='car-detail',
    ),
    url(
        r'^api/v1/cars/(?P<car_pk>\d+)/treatments/$',
        TreatmentListByCarAPIView.as_view(),
        name='treatment-list',
    ),
    url(
        r'^api/v1/cars/(?P<car_pk>\d+)/treatments/(?P<pk>\d+)/$',
        TreatmentDetailByCarAPIView.as_view(),
        name='treatment-detail',
    ),
    # We need the following shallow endpoints to comply with what ember-data
    # expects
    url(
        r'^api/v1/treatments/$',
        TreatmentListAPIView.as_view(),
        name='treatment-list-shallow',
    ),
    url(
        r'^api/v1/treatments/(?P<pk>\d+)/$',
        TreatmentDetailAPIView.as_view(),
        name='treatment-detail-shallow',
    ),

    url(
        r'^api/v1/get-auth-token/',
        'users.views.get_auth_token',
        name='get-auth-token',
    ),
    url(
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),

    # Admin
    url(r'^admin/', include(admin.site.urls)),

    # Index
    url(r'^$', HomePageView.as_view(), name='home'),

    # BrowserID
    (r'^browserid/page/', BrowserIDPageView.as_view()),
    (r'^browserid/', include('django_browserid.urls')),
)
