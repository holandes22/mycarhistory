from django.conf.urls.defaults import patterns, url
from mycarhistory.mechanics.views import MechanicMainView, MechanicDetailView


urlpatterns = patterns('mycarhistory.mechanics.views',
                url(r'main/$', MechanicMainView.as_view(), name='mechanics-main'),
                url(r'mechanic/(?P<pk>\d+)/details/$', MechanicDetailView.as_view(), name='mechanic-detail'),
                )
