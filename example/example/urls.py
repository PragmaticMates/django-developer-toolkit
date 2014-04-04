from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView


admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Examples:
    url(r'^$', TemplateView.as_view(template_name='example/home.html'), name='home'),
)


if 'developer_toolkit' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^toolkit/', include('developer_toolkit.urls')),
    )
