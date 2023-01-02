from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from apps.budget.services import create_balance


@login_required(login_url="users:login")
def add_new_balance(request):
    print(request.POST)
    create_balance(request)
    return redirect("budget:balances")
