from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'paint.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   
    url(r'^$','mypaint.views.paint'),
    url(r'^gallery/$','mypaint.views.gallery'),
    url(r'^gallery/(?P<imagename>[-a-zA-Z0-9]+)/?$', 'mypaint.views.gallery'),
)
