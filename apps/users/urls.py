from django.urls import path

from apps.users.views.login_user import login_user
from apps.users.views.logout_user import logout_user
from apps.users.views.register_user import register_user


app_name = "users"

urlpatterns = [
    path("login/", login_user, name="login"),
    path("register/", register_user, name="register"),
    path("logout/", logout_user, name="logout"),
]
