# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # previous login view
    #path('login/', views.user_login, name='login'),

    url('^', views.profile, name='profile'),

    #форма входа пользователя
    url('^login/', auth_views.LoginView.as_view(), name='login' ),

    #Выход с окаунта пользователя
   url('^logout/', auth_views.LogoutView.as_view(), name='logout'),

    url('^', views.dashboard, name='dashboard'),

    #сменить пароль Представление PasswordChangeView будет обрабатывать форму для изменения пароля

     url('^password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),


    #а представление PasswordChangeDoneView будет отображать сообщение обуспешном завершении после того,
    # как пользователь успешно изменил свойпароль.
    url('^password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # восстановления пароля
    url('^password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset' ),

    url('^password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    url('^reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    url('^reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    #Представление для создания учетных записей пользователей
    url('^register/', views.register, name='register'),

    # редактировать профиль
    url('^edit/', views.edit, name='edit'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)