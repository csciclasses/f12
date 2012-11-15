from django.http import HttpResponse


def index(request):
    return HttpResponse('Auth Index View') 


def new_user(request):
    return HttpResponse('Auth New User View') 


def login(request):
    return HttpResponse('Auth New User View') 
