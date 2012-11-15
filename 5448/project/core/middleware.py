

class AuthMiddleware:
    def process_request(self, request):
        user = request.session.get('user', {'YEAH':'TESTING'})
        request.user = user
        return None
