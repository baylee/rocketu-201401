from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'social_auth_tutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url('^$', 'feed.views.home', name='home'),

    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^admin/', include(admin.site.urls)),
)
