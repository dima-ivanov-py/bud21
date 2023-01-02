from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


@login_required(login_url="budget:login")
def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect("budget:index")
    return render(request, "budget/logout_confirm.html")
