from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from budget.models import Profit
from budget.forms import ProfitEditForm
from budget.services import update_profit


@login_required(login_url="budget:login")
def edit_profit(request, profit_pk):
    profit = get_object_or_404(Profit, pk=profit_pk)
    if request.user.pk != profit.user.pk:
        return HttpResponseNotFound()
    form = ProfitEditForm(instance=profit)
    if request.method == "POST":
        update_profit(request, profit)
        return redirect("budget:profits")
    return render(request, "budget/edit_profit.html", {"form": form})
