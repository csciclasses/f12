from django.http import HttpResponse
from django.shortcuts import render, redirect
from auth import forms, models
from django.views.decorators.csrf import csrf_protect
#from google.appengine.api import memcache


@csrf_protect
def index(request):
    form = forms.LoginForm()
    return render(request, 'index.html', locals())


@csrf_protect
def new_user(request):
    if request.method == 'GET':
        form = forms.NewUserForm()
    else:
        form = forms.NewUserForm(request.POST)
        if form.is_valid():
            resp = models.User.create(form.cleaned_data['email'], form.cleaned_data['password'])
            if resp['status'] == 'UserCreated':
                return redirect('auth-user-created')
    return render(request, 'new_user.html', locals())


def user_created(request):
    return render(request, 'user_created.html', locals())


def validate(request, token):
    resp = models.User.validate(token)
    return render(request, 'validate.html', locals())


@csrf_protect
def login(request):
    form = forms.LoginForm(request.POST)
    if form.is_valid():
        resp = models.User.authenticate(form.cleaned_data['email'], form.cleaned_data['password'])

        if resp['status'] == 'Authenticated':
            request.session['user'] = resp
            #request.session.save()
            #memcache.add('SESSION_%s' % request.session.session_key, resp, 60)
            return redirect('dashboard')

    return render(request, 'index.html', locals())


def logout(request):
    #memcache.delete('SESSION_%s' % request.sessionid)
    request.session.clear()
    return HttpResponse('Logout')
