from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from apps.budget.models import Expense
from apps.budget.forms import ExpenseEditForm
from apps.budget.services import update_expense


@login_required(login_url="users:login")
def edit_expense(request, expense_pk):
    expense = get_object_or_404(Expense, pk=expense_pk)
    if request.user.pk != expense.user.pk:
        return HttpResponseNotFound()
    form = ExpenseEditForm(instance=expense)
    if request.method == "POST":
        update_expense(request, expense)
        return redirect("budget:expenses")
    return render(request, "budget/edit_expense.html", {"form": form})
