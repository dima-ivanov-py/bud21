from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


@login_required(login_url="users:login")
def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect("index")
    return render(request, "users/logout_confirm.html")
