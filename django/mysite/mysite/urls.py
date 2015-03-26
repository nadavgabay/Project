# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
import controller

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # These URLs are necessary for this Temboo example
    url(r'^$', controller.home, name='home'),
    url(r'^search_with_and/', controller.get_login_url_to_serach_with_and, name='search_with_and'),
    url(r'^pick/profile/$', controller.get_user_info, name='profile')
)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# ... the rest of your URLconf goes here ...

urlpatterns += staticfiles_urlpatterns()