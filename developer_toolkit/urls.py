from django.conf.urls import patterns, url

from views import DebugErrorTemplateView, RaiseExceptionView, SettingsView, DebugEmailView, EnvironmentView


urlpatterns = patterns('',
    url(r'^environment/$', EnvironmentView.as_view(), name='toolkit_environment'),
    url(r'^mail/', DebugEmailView.as_view(), name='toolkit_mail'),
    url(r'^error-template/', DebugErrorTemplateView.as_view(), name='toolkit_error_template'),
    url(r'^exception/', RaiseExceptionView.as_view(), name='toolkit_exception'),
    url(r'^settings/', SettingsView.as_view(), name='toolkit_settings'),
)
