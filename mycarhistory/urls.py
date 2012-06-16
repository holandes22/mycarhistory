from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

from mycarhistory.settings import STATIC_ROOT, DEBUG
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^cars/', include('mycarhistory.cars.urls')),
    #url(r'^mechanic/', include('mycarhistory.mechanics.urls')),
)

if DEBUG:
    urlpatterns += patterns(url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT}),)
