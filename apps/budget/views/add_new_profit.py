from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from apps.budget.services import create_profit


@login_required(login_url="users:login")
def add_new_profit(request):
    create_profit(request)
    return redirect("budget:profits")
