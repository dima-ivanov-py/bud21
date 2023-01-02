from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url="users:login")
def index(request):
    return redirect("budget:balances")


urlpatterns = [
    path("", index, name="index"),
    path("admin/", admin.site.urls),
    path("budget/", include("apps.budget.urls")),
    path("users/", include("apps.users.urls")),
]
