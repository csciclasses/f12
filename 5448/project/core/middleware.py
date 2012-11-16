class AuthMiddleware:
    def process_request(self, request):
        user = request.session.get('user')
        request.user = user
        return None

