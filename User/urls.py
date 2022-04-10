from django.urls import path
from . import views

app_name="User"

urlpatterns=[
    path("register/",views.register,name="register"),
    path("login/",views.Userlogin,name="login"),
    path("logout/",views.UserLogout, name="logout")
]