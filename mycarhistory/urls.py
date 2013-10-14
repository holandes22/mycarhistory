from django.contrib import admin
from django.conf import settings
from django.conf.urls import patterns, include, url

from rest_framework import routers

from mycarhistory.views import HomePageView
from mycarhistory.cars.views import CarByUserViewSet
from mycarhistory.treatments.views import TreatmentByCarViewSet


admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'cars', CarByUserViewSet)
router.register(r'cars/(?P<car_pk>\d+)/treatments', TreatmentByCarViewSet)

urlpatterns = patterns('',
    # API
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Admin
    url(r'^admin/', include(admin.site.urls)),

    # Index
    url(r'^$', HomePageView.as_view(), name='home'),

    # BrowserID
    (r'^browserid/', include('django_browserid.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
        (r'^rest_framework/(?P<path>.*)$', 'django.views.static.serve', {}),
    )
