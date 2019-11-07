# -*- coding: utf-8 -*-

from  django.contrib.auth import  views
from django.conf.urls import url

urlpatterns = [
    # Авторизация пользователей с помощью LoginView
    url('login/', views.LoginView.as_view(), name='login'),
    #для выхода,LogoutView
    url('logout/', views.LogoutView.as_view(), name='logout'),
]