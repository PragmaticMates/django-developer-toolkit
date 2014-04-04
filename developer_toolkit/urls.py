from django.conf.urls import patterns, url

from views import DebugErrorView, SettingsView, DebugEmailView, EnvironmentView


urlpatterns = patterns('',
    url(r'^environment/$', EnvironmentView.as_view(), name='toolkit_environment'),
    url(r'^mail/', DebugEmailView.as_view(), name='toolkit_mail'),
    url(r'^error/', DebugErrorView.as_view(), name='toolkit_error'),
    url(r'^settings/', SettingsView.as_view(), name='toolkit_settings'),
)
