from core.utils import ViewDecorators
from django.shortcuts import render


@ViewDecorators.require_user
def index(request):
    return render(request, 'dashboard_index.html')
