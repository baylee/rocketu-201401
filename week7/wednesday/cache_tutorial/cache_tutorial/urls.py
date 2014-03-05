from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cache_tutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'cache.views.index', name='index'),

    url(r'^weather/$', 'cache.views.weather', name='weather'),

    url(r'^admin/', include(admin.site.urls)),
)
