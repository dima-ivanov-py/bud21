from django.urls import path, include

from . import views_old


app_name = "budget"
urlpatterns = [
    path("", views_old.index, name="index"),
    path("login/", views_old.login_user, name="login"),
    path("register/", views_old.register_user, name="register"),
    path("logout/", views_old.logout_user, name="logout"),
    path("balances/", views_old.get_balances_page, name="balances"),
    path("profits/", views_old.get_profits_page, name="profits"),
    path("expenses/", views_old.get_expenses_page, name="expenses"),
    path("balance/new/", views_old.add_new_balance, name="create_balance"),
    path("profit/new/", views_old.add_new_profit, name="create_profit"),
    path("expense/new/", views_old.add_new_expense, name="create_expense"),
    path(
        "balance/<int:balance_pk>/edit/",
        views_old.edit_balance,
        name="edit_balance",
    ),
    path(
        "profit/<int:profit_pk>/edit/", views_old.edit_profit, name="edit_profit"
    ),
    path(
        "expense/<int:expense_pk>/edit/",
        views_old.edit_expense,
        name="edit_expense",
    ),
    path(
        "balance/<int:balance_pk>/delete/",
        views_old.balance_deletion,
        name="delete_balance",
    ),
    path(
        "profit/<int:profit_pk>/delete/",
        views_old.profit_deletion,
        name="delete_profit",
    ),
    path(
        "expense/<int:expense_pk>/delete/",
        views_old.expense_deletion,
        name="delete_expense",
    ),
]
