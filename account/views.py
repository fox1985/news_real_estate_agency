# -*- coding: utf-8 -*-
from django.shortcuts import render
from  django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm

from django.contrib.auth.decorators import login_required
from .models import Profile
#отправка собщений пользовтелю
from django.contrib import messages


def user_login(request):
    if request.method == 'POST':
        'Создаем экземпляр формы с представленными данными помощью form = LoginForm(request.POST)'
        form = LoginForm(request.POST)
        'проверяет правельно ли за полнена формы с помощью form.is_valid() '
        if form.is_valid():
            cd = form.cleaned_data
            'Если предоставленные данные действительны, мы аутентифицируем пользователя по базе данных, используя метод authenticate ()'
            user = authenticate(request, username=cd['username'],
                                         password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Аутентифицировано успешно')
                else:
                    return HttpResponse('Отключенный аккаунт')

            else:
                return HttpResponse('Неправильный логин')
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form' : form})


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'} )




def register(request):
    'Представление для создания учетных записей пользователей'
    if request.method =='POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            'Создайте новый объект пользователя, но пока не сохраняйте его'
            new_user = user_form.save(commit=False)
            'Установить пароль'
            new_user.set_password(user_form.cleaned_data['password'])
            'Сохранить объект пользователя'
            new_user.save()
            'Создать профиль пользователя'
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()

    return render(request, 'account/register.html', {'user_form': user_form})



# Мы используем декоратор login_required , потому что пользователи должны проходить аутентификацию для редактирования своего профиля.
@login_required
def edit(request):
    """""Теперь мы разрешим пользователям редактировать их профиль. чтобы неболо ошибки User has no profile. в модели profiles Должин быть  хоть одного пользователя """
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)

        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            'отправка собщений пользовтелю'
            messages.success(request, 'Профиль обновлен', 'успешно')

        else:
            messages.error(request, 'Ошибка')

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form })





