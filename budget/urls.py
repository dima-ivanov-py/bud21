from django.urls import path

from budget.views.add_new_balance import add_new_balance
from budget.views.add_new_expense import add_new_expense
from budget.views.add_new_profit import add_new_profit
from budget.views.balance_deletion import balance_deletion
from budget.views.edit_balance import edit_balance
from budget.views.edit_expense import edit_expense
from budget.views.edit_profit import edit_profit
from budget.views.expense_deletion import expense_deletion
from budget.views.get_balances_page import get_balances_page
from budget.views.get_expenses_page import get_expenses_page
from budget.views.get_profits_page import get_profits_page
from budget.views.index import index
from budget.views.login_user import login_user
from budget.views.logout_user import logout_user
from budget.views.profit_deletion import profit_deletion
from budget.views.register_user import register_user


app_name = "budget"

urlpatterns = [
    path("", index, name="index"),
    path("login/", login_user, name="login"),
    path("register/", register_user, name="register"),
    path("logout/", logout_user, name="logout"),
    path("balances/", get_balances_page, name="balances"),
    path("profits/", get_profits_page, name="profits"),
    path("expenses/", get_expenses_page, name="expenses"),
    path("balance/new/", add_new_balance, name="create_balance"),
    path("profit/new/", add_new_profit, name="create_profit"),
    path("expense/new/", add_new_expense, name="create_expense"),
    path("balance/<int:balance_pk>/edit/", edit_balance, name="edit_balance"),
    path("profit/<int:profit_pk>/edit/", edit_profit, name="edit_profit"),
    path("expense/<int:expense_pk>/edit/", edit_expense, name="edit_expense"),
    path(
        "balance/<int:balance_pk>/delete/",
        balance_deletion,
        name="delete_balance",
    ),
    path(
        "profit/<int:profit_pk>/delete/", profit_deletion, name="delete_profit"
    ),
    path(
        "expense/<int:expense_pk>/delete/",
        expense_deletion,
        name="delete_expense",
    ),
]
