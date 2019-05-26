# -*- coding: utf-8 -*-
from django import forms


# Модель формы обратной связи
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    nomer = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
