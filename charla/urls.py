from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'charla.views.home', name='home'),
    # url(r'^charla/', include('charla.foo.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/(?P<user_type>user|actor)/$', 'registration.views.register_user', name='registro'),
    url(r'^review/(?P<movie_id>\d+)/$', 'registration.views.add_review', name='add_review'),
)
