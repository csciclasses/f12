from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
import hashlib
import base64


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
