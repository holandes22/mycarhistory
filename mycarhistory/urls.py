from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from rest_framework import routers

from mycarhistory.cars.views import CarViewSet, CarByUserViewSet
from mycarhistory.users.views import UserViewSet
from mycarhistory.treatments.views import TreatmentViewSet

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'cars', CarViewSet,)
router.register(r'users', UserViewSet)
router.register(r'treatments', TreatmentViewSet)

car_router = routers.DefaultRouter()
car_router.register(r'cars', CarByUserViewSet,)


urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api/users/(?P<user_pk>\d+)/', include(car_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('', 
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
        (r'^rest_framework/(?P<path>.*)$', 'django.views.static.serve', {}),
    )
