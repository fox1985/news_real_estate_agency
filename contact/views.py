# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from django.http import HttpResponse
from contact.forms import ContactForm

# Create your views here.


# Функция формы обратной связи
def contactform(reguest):
    if reguest.method == 'POST':
        form = ContactForm(reguest.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            nomer = form.cleaned_data['nomer']

            # словарь куда водится почта пользователя
            recipients = []

            recipients.append(sender)

            send_mail(subject, message, sender, nomer,  recipients)
            return render(reguest, 'contact/thanks.html')

    else:
        form = ContactForm()
    # Выводим форму в шаблон
    return render(reguest, 'contact/contact.html', {'form': form})



