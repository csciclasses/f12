from core.utils import ViewDecorators
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from dashboard import forms, models


@csrf_protect
@ViewDecorators.require_user
def index(request):
    activity_type_list = models.ActivityType.get_user_activity_type_list(request.user['email'])

    if request.method == 'GET':
        form = forms.CreateActivityForm()
        form.prepare(activity_type_list)
    else:
        form = forms.CreateActivityForm(request.POST)
        form.prepare(activity_type_list)
        if form.is_valid():
            resp = models.Activity.create_activity(request.user['email'], form.cleaned_data)
    return render(request, 'index.html', locals())


@csrf_protect
@ViewDecorators.require_user
def create_activity_type(request):
    if request.method == 'GET':
        form = forms.AddActivityTypeForm()
    else:
        form = forms.AddActivityTypeForm(request.POST)
        if form.is_valid():
            resp = models.ActivityType.create_activity_type(request.user['email'], form.cleaned_data['name'])
            if resp['status'] == 'ActivityCreated':
                return redirect('dashboard')
    return render(request, 'create_type.html', locals())
