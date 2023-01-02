from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("budget:index")
        else:
            messages.info(request, "login or password is incorrect")
    return render(request, "budget/login.html")
