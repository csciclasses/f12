from core import models
#from google.appengine.api import memcache


class AuthMiddleware:
    def process_request(self, request):
        request_id = request.META.get('REQUEST_ID_HASH')
        if request_id:
            models.RequestLog.save(request_id)

        user = request.session.get('user')
        #user = None
        #sessionid = request.COOKIES.get('sessionid')
        #if sessionid:
        #    user = memcache.get('SESSION_%s' % sessionid)
        request.user = user
        #request.sessionid = sessionid
        return None
