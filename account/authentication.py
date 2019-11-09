# -*- coding: utf-8 -*-
'Построение собственной серверной аутентификации 248'
from django.contrib.auth.models import User

class EmailAuthBackend(object):
    """Аутентификация с использованием адреса электронной почты."""
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.chek_password(password):
                return user
            return None

        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


        
