# -*- coding: utf-8 -*-
from django import forms

class ContactForm (forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    nomer = forms.CharField(max_length=30)
    message = forms.CharField(max_length=2000, widget=forms.Textarea, required=True)





