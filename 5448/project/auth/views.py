from django.http import HttpResponse
from django.shortcuts import render
from auth import forms
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def index(request):
    form = forms.LoginForm()
    return render(request, 'auth/index.html', locals())


def new_user(request):
    return HttpResponse('Auth New User View')


@csrf_protect
def login(request):
    form = forms.LoginForm(request.POST)
    if form.is_valid():
        pass
    return render(request, 'auth/index.html', locals())


def logout(request):
    return HttpResponse('Logout')
