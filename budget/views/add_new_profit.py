from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from budget.services import create_profit


@login_required(login_url="budget:login")
def add_new_profit(request):
    create_profit(request)
    return redirect("budget:profits")
