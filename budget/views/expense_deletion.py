from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from budget.models import Expense
from budget.services import del_expense


@login_required(login_url="budget:login")
def expense_deletion(request, expense_pk):
    expense = get_object_or_404(Expense, pk=expense_pk)
    if request.user.pk != expense.user.pk:
        return HttpResponseNotFound()
    if request.method == "POST":
        del_expense(request, expense)
        return redirect("budget:expenses")
    return render(
        request, "budget/expense_del_confirm.html", {"expense": expense}
    )
