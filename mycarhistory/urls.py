from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from rest_framework import routers

from mycarhistory.cars.views import CarViewSet, CarByUserListView
from mycarhistory.treatments.views import TreatmentViewSet, TreatmentByCarListView

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'treatments', TreatmentViewSet)

urlpatterns = patterns('',
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/users/(?P<user_pk>\d+)/cars', CarByUserListView.as_view()),
    url(r'^api/v1/cars/(?P<car_pk>\d+)/treatments', TreatmentByCarListView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
        (r'^rest_framework/(?P<path>.*)$', 'django.views.static.serve', {}),
    )
