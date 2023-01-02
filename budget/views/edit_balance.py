from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from budget.models import Balance
from budget.forms import BalanceEditForm
from budget.services import update_balance


@login_required(login_url="budget:login")
def edit_balance(request, balance_pk):
    balance = get_object_or_404(Balance, pk=balance_pk)
    if request.user.pk != balance.user.pk:
        return HttpResponseNotFound()
    form = BalanceEditForm(instance=balance)
    if request.method == "POST":
        update_balance(request, balance)
        return redirect("budget:balances")
    return render(request, "budget/edit_balance.html", {"form": form})
