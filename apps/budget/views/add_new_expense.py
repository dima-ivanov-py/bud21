from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from apps.budget.services import create_expense


@login_required(login_url="users:login")
def add_new_expense(request):
    create_expense(request)
    return redirect("budget:expenses")
