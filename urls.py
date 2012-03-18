from django.conf.urls.defaults import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = \
patterns('',
         url(r'^$', 'simmonsdash.views.home', name='home'),
         url(r'^calendar/', 'simmonsdash.views.calendar', name='calendar'),
         url(r'^events/', 'simmonsdash.views.events', name='events'),
         url(r'^nextbus/', 'simmonsdash.nextbus.nextbus', name='nextbus'),
         url(r'^weather/', 'simmonsdash.views.weather', name='weather'),
         url(r'^news/', 'simmonsdash.views.news', name='news'),
         url(r'^localnews/', 'simmonsdash.views.localnews', name='news'),
         url(r'^light', 'simmonsdash.views.light', name='light'),
         url(r'^editorial', 'simmonsdash.views.editorial', name='light'),
         url(r'^posters/', 'simmonsdash.views.posters', name='posters'),
         
    # url(r'^simmonsdash/', include('simmonsdash.foo.urls')),
         url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
             'document_root': settings.MEDIA_ROOT,
             }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
             'document_root': settings.STATIC_ROOT,
             }),   

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
