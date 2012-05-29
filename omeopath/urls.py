from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from apps.coming_soon.views import CreateProspect

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^gerd/$', TemplateView.as_view(template_name='coming_soon/coming_soon.html')),
    url(r'^gerd/notification_signup/$', CreateProspect.as_view(), name="notification_signup"), 
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
