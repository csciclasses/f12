from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import redirect
import hashlib
import base64


def user_view_context_processor(request):
    return {'user': request.user}


class ViewDecorators:
    #Checks session user. If not presents Logs user out
    @staticmethod
    def require_user(func):
        def require_user_inner(request, *args, **kwargs):
            if not request.user:
                return redirect('index')
            else:
                return func(request, *args, **kwargs)
        return require_user_inner


class EncUtil:
    @staticmethod
    def encrypt(value):
        if not isinstance(value, basestring):
            raise ValueError('Value to has must be of type string')
        return base64.encodestring(value)

    @staticmethod
    def decrypt(value):
        if not isinstance(value, basestring):
            raise ValueError('Value to has must be of type string')
        return base64.decodestring(value)

if not hasattr(settings, 'APP_SECRET'):
    raise ImproperlyConfigured('Encryption Key must be properly defined')


class HashUtil:
    @staticmethod
    def hash(value):
        if not isinstance(value, basestring):
            raise ValueError('Value to has must be of type string')
            return hashlib.sha512(value).hexdigest().upper()
