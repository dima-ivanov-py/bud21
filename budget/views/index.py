from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url="budget:login")
def index(request):
    return redirect("budget:balances")
