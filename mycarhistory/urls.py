from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from rest_framework import routers

from mycarhistory.users.views import UserViewSet
from mycarhistory.cars.views import CarViewSet, CarByUserViewSet
from mycarhistory.treatments.views import TreatmentViewSet, TreatmentByCarViewSet

admin.autodiscover()

router = routers.DefaultRouter()

# Admin API
router.register(r'cars', CarViewSet,)
router.register(r'users', UserViewSet)
router.register(r'treatments', TreatmentViewSet)
router.register(r'cars/(?P<car_pk>\d+)/treatments', TreatmentByCarViewSet)

# Regular user API
router.register(r'users/(?P<user_pk>\d+)/cars', CarByUserViewSet)
router.register(r'users/(?P<user_pk>\d+)/cars/(?P<car_pk>\d+)/treatments', TreatmentByCarViewSet)


urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),  # For admins
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('', 
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
        (r'^rest_framework/(?P<path>.*)$', 'django.views.static.serve', {}),
    )
