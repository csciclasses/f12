from django.http import HttpResponse
from django.shortcuts import render
from auth import forms
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def index(request):
    form = forms.LoginForm()
    return render(request, 'auth/index.html', locals())


@csrf_protect
def new_user(request):
    if request.method == 'GET':
        form = forms.NewUserForm()
    else:
        form = forms.NewUserForm(request.POST)
        if form.is_valid():
            return HttpResponse('NewUser - {0}'.format(form.cleaned_data))
    return render(request, 'auth/new_user.html', locals())


@csrf_protect
def login(request):
    form = forms.LoginForm(request.POST)
    if form.is_valid():
        return HttpResponse('Login - {0}'.format(form.cleaned_data))
    return render(request, 'auth/index.html', locals())


def logout(request):
    return HttpResponse('Logout')
