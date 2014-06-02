from django.template.loader import get_template

__author__ = 'Erik Telepovsky'

import json
import locale
import os
import sys

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

from django.conf import settings
from django.core import mail
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest
from django.template.base import TemplateDoesNotExist
from django.utils.translation import ugettext, ugettext_lazy as _
from django.views.generic import TemplateView, View, FormView

from forms import DebugEmailForm


class EnvironmentView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated() or not request.user.is_superuser:
            return HttpResponseForbidden('You have to be logged in as superuser')

        loc_info = "<h1>Locale settings:</h1>" + \
            "getlocale: " + str(locale.getlocale()) + \
            "<br/>getdefaultlocale(): " + str(locale.getdefaultlocale()) + \
            "<br/>fs_encoding: " + str(sys.getfilesystemencoding()) + \
            "<br/>sys default encoding: " + str(sys.getdefaultencoding())

        environ = "<h1>Environment constants:</h1>"

        for key in OrderedDict(sorted(os.environ.items())):
            environ += '<br/>%s: %s' % (key, os.environ[key])
        return HttpResponse(loc_info + '<br/>' + environ)


class DebugErrorTemplateView(TemplateView):
    template_name = '500.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated() or not request.user.is_superuser:
            return HttpResponseForbidden('You have to be logged in as superuser')

        try:
            get_template(self.template_name)
        except TemplateDoesNotExist:
            return HttpResponseBadRequest(_(u'Template with name "%s" does not exist.' % self.template_name))

        return super(DebugErrorTemplateView, self).dispatch(request, *args, **kwargs)


class RaiseExceptionView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated() or not request.user.is_superuser:
            return HttpResponseForbidden('You have to be logged in as superuser')
        raise Exception(ugettext('This Exception was raised by DebugErrorView of django-developer-toolkit library.'))


class SettingsView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated() or not request.user.is_superuser:
            return HttpResponseForbidden('You have to be logged in as superuser')

        settings_dict = dict()
        for key in dir(settings):
            value = getattr(settings, key, None)

            if isinstance(value, basestring) or isinstance(value, tuple) \
                or isinstance(value, list) or isinstance(value, bool)\
                or value is None or isinstance(value, int):
                settings_dict[key] = value
            else:
                try:
                    if isinstance(value, dict):
                        try:
                            json.dumps(value)
                            settings_dict[key] = value
                        except TypeError:
                            #print key, type(value)
                            settings_dict[key] = unicode(value)
                    else:
                        #print key, type(value)
                        settings_dict[key] = unicode(value)
                except Exception as e:
                    settings_dict[key] = unicode(e)

        settings_dict = OrderedDict(sorted(settings_dict.items()))
        return self.return_response(settings_dict)

    def return_response(self, obj, response_class=HttpResponse):
        response = response_class(
            json.dumps(obj, indent=4, separators=(',', ': ')),
            content_type='application/json'
        )
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response


class DebugEmailView(FormView):
    template_name = 'developer_toolkit/mail_form.html'
    form_class = DebugEmailForm

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated() or not request.user.is_superuser:
            return HttpResponseForbidden('You have to be logged in as superuser')
        return super(DebugEmailView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        try:
            data = form.cleaned_data

            # from
            from_email = u'%s <%s>' % (data['email_from_name'], data['email_from'])

            # to
            recipients = []
            for recipient in data['to'].split(','):
                recipients.append(recipient.strip())

            recipients_list = u", ".join(recipients)

            # subject
            subject = data['subject']

            # create new connection
            connection = mail.get_connection(backend=data['email_backend'])
            connection.password = str(data['email_host_password'])
            connection.username = data['email_host_user']
            connection.host = data['email_host']
            connection.port = data['email_port']
            connection.use_tls = data['email_use_tls']

            # message
            ip_address = self.request.META.get('REMOTE_ADDR', '')
            message_html = u'This email came from %s and was sent by %s.<br>' % (getattr(settings, 'HOST_URL', ip_address), self.request.user)
            for key in data:
                message_html += u"<br>%s: %s" % (key, data[key])

            msg = EmailMultiAlternatives(subject, '', from_email, recipients, connection=connection)
            msg.attach_alternative(message_html, "text/html")

            success = msg.send(fail_silently=False)
            if success:
                message = 'Email was sent to %s by %s.' % (recipients_list, self.request.user)
                return self.render_to_response(self.get_context_data(form=form, message=message))
            else:
                message = 'ERROR: Email was NOT sent!'
                return self.render_to_response(self.get_context_data(form=form, message=message))

        except Exception as e:
            message = str(e)
            return self.render_to_response(self.get_context_data(form=form, message=message, message_class='error'))
