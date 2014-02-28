from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'hollywood.views.home', name='home'),

    url(r'^movies/$', 'hollywood.views.movies', name='movies'),
    url(r'^movies/new/$', 'hollywood.views.new_movie', name='new_movie'),
    url(r'^movies/(?P<movie_id>\w+)/$', 'hollywood.views.view_movie', name='view_movie'),
    url(r'^movies/(?P<movie_id>\w+)/edit/$', 'hollywood.views.edit_movie', name='edit_movie'),
    url(r'^movies/(?P<movie_id>\w+)/delete/$', 'hollywood.views.delete_movie', name='delete_movie'),

    url(r'^actors/$', 'hollywood.views.actors', name='actors'),

    url(r'^ajaxiness/$', 'hollywood.views.ajaxiness', name='ajaxiness'),
    url(r'^more_information/$', 'hollywood.views.more_information', name='more_information'),
)
