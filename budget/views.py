from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum

from .models import Balance, Profit, Expense
from .forms import BalanceEditForm, ProfitEditForm, ExpenseEditForm
from .services import (create_balance, create_profit, create_expense,
                       get_balances, get_profits, get_expenses,
                       update_balance, update_profit, update_expense,
                       del_profit, del_expense, get_csv_file, paginate_query)


@login_required(login_url='budget:login')
def index(request):
    return redirect('budget:balances')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('budget:index')
        else:
            messages.info(request, 'login or password is incorrect')
    return render(request, 'budget/login.html')


def register_user(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('budget:index')
    return render(request, 'budget/register.html', {'form':form})


@login_required(login_url='budget:login')
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('budget:index')
    return render(request, 'budget/logout_confirm.html')


@login_required(login_url='budget:login')
def get_balances_page(request):
    balances = get_balances(request)
    page_obj = paginate_query(request, balances)
    context = {
        'balances': balances,
        'page_obj': page_obj,
        'total': balances.aggregate(Sum('total'))['total__sum'],
    }
    return render(request, 'budget/balances.html', context)


@login_required(login_url='budget:login')
def get_profits_page(request):
    profits = get_profits(request)
    page_obj = paginate_query(request, profits)
    context = {
        'profits': profits,
        'page_obj': page_obj,
        'total': profits.aggregate(Sum('total'))['total__sum'],
    }
    if request.method == 'POST':
        return get_csv_file(request, profits)
    return render(request, 'budget/profits.html', context)


@login_required(login_url='budget:login')
def get_expenses_page(request):
    expenses = get_expenses(request)
    page_obj = paginate_query(request, expenses)
    context = {
        'expenses': expenses,
        'page_obj': page_obj,
        'total': expenses.aggregate(Sum('total'))['total__sum'],
    }
    if request.method == 'POST':
        return get_csv_file(request, expenses)
    return render(request, 'budget/expenses.html', context)


@login_required(login_url='budget:login')
def add_new_balance(request):
    print(request.POST)
    create_balance(request)
    return redirect('budget:balances')


@login_required(login_url='budget:login')
def add_new_profit(request):
    create_profit(request)
    return redirect('budget:profits')


@login_required(login_url='budget:login')
def add_new_expense(request):
    create_expense(request)
    return redirect('budget:expenses')


@login_required(login_url='budget:login')
def edit_balance(request, balance_pk):
    balance = get_object_or_404(Balance, pk=balance_pk)
    if request.user.pk != balance.user.pk:
        return HttpResponseNotFound()
    form = BalanceEditForm(instance=balance)
    if request.method == 'POST':
        update_balance(request, balance)
        return redirect('budget:balances')
    return render(request, 'budget/edit_balance.html', {'form': form})


@login_required(login_url='budget:login')
def edit_profit(request, profit_pk):
    profit = get_object_or_404(Profit, pk=profit_pk)
    if request.user.pk != profit.user.pk:
        return HttpResponseNotFound()
    form = ProfitEditForm(instance=profit)
    if request.method == 'POST':
        update_profit(request, profit)
        return redirect('budget:profits')
    return render(request, 'budget/edit_profit.html', {'form': form})


@login_required(login_url='budget:login')
def edit_expense(request, expense_pk):
    expense = get_object_or_404(Expense, pk=expense_pk)
    if request.user.pk != expense.user.pk:
        return HttpResponseNotFound()
    form = ExpenseEditForm(instance=expense)
    if request.method == 'POST':
        update_expense(request, expense)
        return redirect('budget:expenses')
    return render(request, 'budget/edit_expense.html', {'form': form})


@login_required(login_url='budget:login')
def balance_deletion(request, balance_pk):
    balance = get_object_or_404(Balance, pk=balance_pk)
    if request.user.pk != balance.user.pk:
        return HttpResponseNotFound()
    if request.method == 'POST':
        balance.delete()
        return redirect('budget:balances')
    return render(request, 'budget/balance_del_confirm.html', {'balance': balance})


@login_required(login_url='budget:login')
def profit_deletion(request, profit_pk):
    profit = get_object_or_404(Profit, pk=profit_pk)
    if request.user.pk != profit.user.pk:
        return HttpResponseNotFound()
    if request.method == 'POST':
        del_profit(request, profit)
        return redirect('budget:profits')
    return render(request, 'budget/profit_del_confirm.html', {'profit': profit})


@login_required(login_url='budget:login')
def expense_deletion(request, expense_pk):
    expense = get_object_or_404(Expense, pk=expense_pk)
    if request.user.pk != expense.user.pk:
        return HttpResponseNotFound()
    if request.method == 'POST':
        del_expense(request, expense)
        return redirect('budget:expenses')
    return render(request, 'budget/expense_del_confirm.html', {'expense': expense})
