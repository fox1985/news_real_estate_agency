# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from  news_real_estate_agency.emailsettings import *

# Функция формы обратной связи

def page_contact(request):
    sent = False
    mailfrom = EMAIL_HOST_USER
    mailto = [EMAIL_HOST_USER]
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = 'Autister - Новое письмо от {}'.format(cd['name'])
            message = 'Прислал {}. \n \n \n Пишет: {}'.format(cd['email'], cd['message'])
            send_mail(subject, message, mailfrom, mailto)
            sent = True
    else:
        form = ContactForm()
    return render(request, 'contact/email.html', {'form': form, 'sent': sent})


