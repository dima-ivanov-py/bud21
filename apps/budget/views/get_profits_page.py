from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.budget.services import (
    get_profits,
    get_csv_file,
    paginate_query,
    get_total,
)


@login_required(login_url="users:login")
def get_profits_page(request):
    profits = get_profits(request)
    page_obj = paginate_query(request, profits)
    total = get_total(profits)
    context = {"profits": profits, "page_obj": page_obj, "total": total}

    if request.method == "POST":
        return get_csv_file(request, profits)

    return render(request, "budget/profits.html", context)
