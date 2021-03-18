from django.urls import path, include

from . import views


app_name = 'budget'
urlpatterns = [
    path('', views.index, name='index'),

    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),

    path('balances/', views.get_balances_page, name='balances'),
    path('profits/', views.get_profits_page, name='profits'),
    path('expenses/', views.get_expenses_page, name='expenses'),

    path('balance/new/', views.add_new_balance, name='create_balance'),
    path('profit/new/', views.add_new_profit, name='create_profit'),
    path('expense/new/', views.add_new_expense, name='create_expense'),

    path('balance/<int:balance_pk>/edit/', views.edit_balance,
        name='edit_balance'),
    path('profit/<int:profit_pk>/edit/', views.edit_profit,
        name='edit_profit'),
    path('expense/<int:expense_pk>/edit/', views.edit_expense,
        name='edit_expense'),

    path('balance/<int:balance_pk>/delete/', views.balance_deletion,
        name='delete_balance'),
    path('profit/<int:profit_pk>/delete/', views.profit_deletion,
        name='delete_profit'),
    path('expense/<int:expense_pk>/delete/', views.expense_deletion,
        name='delete_expense'),
]
