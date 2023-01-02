from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.budget.services import get_balances, paginate_query, get_total


@login_required(login_url="users:login")
def get_balances_page(request):
    balances = get_balances(request)
    page_obj = paginate_query(request, balances)
    total = get_total(balances)
    context = {"balances": balances, "page_obj": page_obj, "total": total}
    return render(request, "budget/balances.html", context)
