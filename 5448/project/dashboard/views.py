from core.utils import ViewDecorators
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from dashboard.models import ActivityType
from dashboard.forms import AddActivityTypeForm


@csrf_protect
@ViewDecorators.require_user
def index(request):
    activity_type_list = ActivityType.get_user_activity_type_list(request.user['email'])
    return render(request, 'dashboard_index.html', locals())


@csrf_protect
@ViewDecorators.require_user
def create_activity_type(request):
    if request.method == 'GET':
        form = AddActivityTypeForm()
    else:
        form = AddActivityTypeForm(request.POST)
        if form.is_valid():
            resp = ActivityType.create_activity_type(request.user['email'], form.cleaned_data['name'])
            if resp['status'] == 'ActivityCreated':
                return redirect('dashboard')
    return render(request, 'create_type.html', locals())
