#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import *
#from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()
import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from views import about
#from djangobb_forum import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
url(r'^$',about) 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#urlpatterns += staticfiles_urlpatterns()
#if settings.DEBUG:
    # static files (images, css, javascript, etc.)
 #   urlpatterns = [
#			url(r'^admin/', include(admin.site.urls)),
#                        url(r"^images/(?P<path>.*)$", "django.views.static.serve",{"document_root": "images",}),
#                        url(r"^css/(?P<path>.*)$", "django.views.static.serve", {"document_root": "css",}),
#                        url(r"^js/(?P<path>.*)$", "django.views.static.serve", {"document_root": "js",}),
#                        url(r"^media/(?P<path>.*)$", "django.views.static.serve", {"document_root": settings.MEDIA_ROOT,}),
#			]

