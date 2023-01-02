from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def register_user(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("budget:index")
    return render(request, "budget/register.html", {"form": form})
