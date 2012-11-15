from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'auth/index.html')


def new_user(request):
    return HttpResponse('Auth New User View')


def login(request):
    return HttpResponse('Auth New User View')
