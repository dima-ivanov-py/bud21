from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.budget.services import (
    get_expenses,
    get_csv_file,
    paginate_query,
    get_total,
)


@login_required(login_url="users:login")
def get_expenses_page(request):
    expenses = get_expenses(request)
    page_obj = paginate_query(request, expenses)
    total = get_total(expenses)
    context = {"expenses": expenses, "page_obj": page_obj, "total": total}

    if request.method == "POST":
        return get_csv_file(request, expenses)

    return render(request, "budget/expenses.html", context)
