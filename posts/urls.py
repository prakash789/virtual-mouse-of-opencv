"""trydjango19 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from.views import (post_list,post_details,post_create,post_update,post_delete,)

urlpatterns = [
    url(r'^$',post_list, name='list'),
    url(r'^(?P<id>\d+)/$',post_details,name='details'),
    url(r'^create$',post_create),
    url(r'^(?P<id>\d+)/edit/$',post_update),
    url(r'^(?P<id>\d+)/delete/$',post_delete,name='delete')
    ]