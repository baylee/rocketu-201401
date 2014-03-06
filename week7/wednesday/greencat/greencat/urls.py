from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
import storefront

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('storefront.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
