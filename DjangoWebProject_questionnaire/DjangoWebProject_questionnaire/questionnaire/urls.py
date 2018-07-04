"""
Definition of urls for DjangoWebProject3.
"""

from django.conf.urls import include, url
from . import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', DjangoWebProject3.views.home, name='home'),
    # url(r'^DjangoWebProject3/', include('DjangoWebProject3.DjangoWebProject3.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
   
    url(r'^questionnaire/$', views.index,name = 'index'),
    url(r'^$', views.mainPage,name = 'main'),
    url(r'^questionnaire/(?P<now_id>[0-9]+)$',views.index_action,name = 'index_action'),
    url(r'^end/$', views.index_action,name = 'index_action'),
    url(r'^start/$', views.startx,name = 'start'),
    url(r'^start/first$',views.callfunc,name = 'callfunc'),
    url(r'^start/download$',views.download_file,name = 'download_file'),
]


