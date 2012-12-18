from core.utils import ViewDecorators
from dashboard.models import Activity, ActivityType
from django.shortcuts import render
from report import forms
from django.views.decorators.csrf import csrf_protect


@csrf_protect
@ViewDecorators.require_user
def index(request):
    activity_type_list = ActivityType.get_user_activity_type_list(request.user['email'])

    if request.method == 'GET':
        form = forms.ActivityListForm()
        form.prepare(activity_type_list)
        filters = {}
    else:
        form = forms.ActivityListForm(request.POST)
        form.prepare(activity_type_list)
        if form.is_valid():
            filters = form.cleaned_data
        else:
            filters = {}

    activity_list = Activity.get_user_activity(request.user['email'], filters)
    return render(request, 'report_index.html', locals())

