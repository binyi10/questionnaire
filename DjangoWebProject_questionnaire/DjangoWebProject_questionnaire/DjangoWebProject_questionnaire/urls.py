"""
Definition of urls for DjangoWebProject_questionnaire.
"""

from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', DjangoWebProject_questionnaire.views.home, name='home'),
    # url(r'^DjangoWebProject_questionnaire/', include('DjangoWebProject_questionnaire.DjangoWebProject_questionnaire.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^questionnaire/', include('questionnaire.urls')),
]
