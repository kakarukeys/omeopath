from django.conf.urls import patterns, include, url

import apps.coming_soon.views as coming_soon

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Coming soon page
    url(r'^gerd/$', coming_soon.ComingSoon.as_view(), name="coming_soon"),
    url(r'^gerd/notification_signup/$', coming_soon.CreateProspect.as_view(), name="notification_signup"),
    url(r'^gerd/download/ebook/(?P<expired_at>[a-z]{10})/(?P<filename>[\w-]+\.[a-z]{3})$', coming_soon.DownloadEbook.as_view(), name="download_ebook"),
    
    # Book checkout via Paypal
    url(r'^gerd/bpwxcwfxk/$', include('paypal.standard.ipn.urls')),
    url(r'^gerd/payment_was_successful/$', coming_soon.PaymentWasSuccessful.as_view(), name="payment_was_successful"),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
