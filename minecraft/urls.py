from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'minecraft.views.home', name='home'),
    # url(r'^minecraft/', include('minecraft.foo.urls')),
	url(r'^$', 'mccatalog.views.home', name='home'),
	url(r'^query/', 'mccatalog.views.getQuanBySymbol', name='query'),
	url(r'^put/', 'mccatalog.views.updateQuanBySymbol', name='put'),
	url(r'^add/', 'mccatalog.views.addSymbol', name='put'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
