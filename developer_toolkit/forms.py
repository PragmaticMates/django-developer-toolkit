from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class DebugEmailForm(forms.Form):
    email_from = forms.EmailField(initial=getattr(settings, 'EMAIL_FROM', None))
    email_from_name = forms.CharField(initial=getattr(settings, 'EMAIL_FROM_NAME', None))
    to = forms.CharField(initial=", ".join(getattr(settings, 'ADMINS_MAILS', '')))
    email_backend = forms.CharField(initial=getattr(settings, 'EMAIL_BACKEND', None))
    email_host = forms.CharField(initial=getattr(settings, 'EMAIL_HOST', None))
    email_host_password = forms.CharField(initial=getattr(settings, 'EMAIL_HOST_PASSWORD', None))
    email_host_user = forms.CharField(initial=getattr(settings, 'EMAIL_HOST_USER', None))
    email_port = forms.IntegerField(initial=getattr(settings, 'EMAIL_PORT', None))
    email_use_tls = forms.BooleanField(initial=getattr(settings, 'EMAIL_USE_TLS', True), required=False)
    subject = forms.CharField(initial=_(u'Debugging email'))
    message = forms.CharField()
