import csv
import codecs
from decimal import Decimal

from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Sum

from .models import Balance, Profit, Expense
from .filters import BalanceFilter, ProfitFilter, ExpenseFilter


def create_balance(request):
    balance = request.user.balance_set.filter(title=request.POST["title"])
    if balance:
        return messages.info(request, "balance with that name already exists")
    Balance.objects.create(
        user=request.user,
        title=request.POST["title"],
        total=request.POST["total"],
    )


def create_profit(request):
    total = request.POST["total"]
    balance = request.user.balance_set.filter(title=request.POST["balance"])
    if balance:
        balance = balance[0]
        balance.total += Decimal(total)
        balance.save()
    else:
        balance = request.POST["balance"]
    Profit.objects.create(
        user=request.user,
        balance=balance,
        title=request.POST["title"],
        description=request.POST["description"],
        total=total,
    )


def create_expense(request):
    total = request.POST["total"]
    balance = request.user.balance_set.filter(title=request.POST["balance"])
    if balance:
        balance = balance[0]
        balance.total -= Decimal(total)
        balance.save()
    else:
        balance = request.POST["balance"]
    Expense.objects.create(
        user=request.user,
        balance=balance,
        title=request.POST["title"],
        description=request.POST["description"],
        total=total,
    )


def get_balances(request):
    balances = request.user.balance_set.all().order_by("-pub_date")
    balance_filter = BalanceFilter(request.GET, queryset=balances)
    return balance_filter.qs


def get_profits(request):
    profits = request.user.profit_set.all().order_by("-pub_date")
    profit_filter = ProfitFilter(request.GET, queryset=profits)
    return profit_filter.qs


def get_expenses(request):
    expenses = request.user.expense_set.all().order_by("-pub_date")
    expense_filter = ExpenseFilter(request.GET, queryset=expenses)
    return expense_filter.qs


def update_balance(request, balance):
    balance.title = request.POST["title"]
    balance.total = request.POST["total"]
    balance.save()


def update_profit(request, profit):
    profit.title = request.POST["title"]
    profit.description = request.POST["description"]
    profit.save()


def update_expense(request, expense):
    expense.title = request.POST["title"]
    expense.description = request.POST["description"]
    expense.save()


def del_profit(request, profit):
    balance = request.user.balance_set.filter(title=profit.balance)
    if balance:
        balance = balance[0]
        balance.total -= profit.total
        balance.save()
    profit.delete()


def del_expense(request, expense):
    balance = request.user.balance_set.filter(title=expense.balance)
    if balance:
        balance = balance[0]
        balance.total += expense.total
        balance.save()
    expense.delete()


def get_csv_file(request, query):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="budget-table.csv"'
    response.write(codecs.BOM_UTF8)
    writer = csv.writer(response, delimiter=",")
    writer.writerow(["BALANCE", "TITLE", "DESCRIPTION", "PUB_DATE", "TOTAL"])
    for item in query:
        writer.writerow(
            [
                item.balance,
                item.title,
                item.description,
                item.pub_date,
                item.total,
            ]
        )
    return response


def paginate_query(request, query):
    paginator = Paginator(query, 3)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)


def get_total(queryset):
    try:
        return round(queryset.aggregate(Sum("total"))["total__sum"], 2)
    except Exception:
        return 0
