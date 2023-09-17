from django.urls import path

from . import views

app_name = "login"

urlpatterns = [
    path("", views.index, name="index"),  # 무시
    path("login/", views.login, name="login"),
    path("receive/", views.receive, name="receive"),
]
