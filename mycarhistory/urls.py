from django.contrib import admin
from django.conf.urls import patterns, include, url

from mycarhistory.users.views import UserListAPIView, UserDetailAPIView
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
        r'^api/v1/auth/login/$',
        'users.views.login',
        name='login',
    ),
    url(
        r'^api/v1/users/$',
        UserListAPIView.as_view(),
        name='user-list',
    ),
    url(
        r'^api/v1/users/(?P<pk>\d+/$)',
        UserDetailAPIView.as_view(),
        name='user-detail',
    ),
    # Admin
    url(r'^admin/', include(admin.site.urls)),
)
