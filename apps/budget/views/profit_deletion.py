from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from apps.budget.models import Profit
from apps.budget.services import del_profit


@login_required(login_url="users:login")
def profit_deletion(request, profit_pk):
    profit = get_object_or_404(Profit, pk=profit_pk)
    if request.user.pk != profit.user.pk:
        return HttpResponseNotFound()
    if request.method == "POST":
        del_profit(request, profit)
        return redirect("budget:profits")
    return render(
        request, "budget/profit_del_confirm.html", {"profit": profit}
    )
