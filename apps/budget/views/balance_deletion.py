from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from apps.budget.models import Balance


@login_required(login_url="users:login")
def balance_deletion(request, balance_pk):
    balance = get_object_or_404(Balance, pk=balance_pk)
    if request.user.pk != balance.user.pk:
        return HttpResponseNotFound()
    if request.method == "POST":
        balance.delete()
        return redirect("budget:balances")
    return render(
        request, "budget/balance_del_confirm.html", {"balance": balance}
    )
