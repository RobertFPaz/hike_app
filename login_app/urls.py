from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register_page', views.register_page),
    path('register', views.register),
    path('login_page', views.login_page),
    path('login', views.login),
    path('logout', views.logout),
]