from django.conf.urls import patterns, include, url
from esih_admin.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pythonfinal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^admins/', include(admin_site.urls)),
    #url(r'^cv/', 'esih_admin.views.dispCV'),
    #url(r'^files/', include('django_bfm.urls')),
)

#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#urlpatterns += staticfiles_urlpatterns()