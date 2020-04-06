# -*- coding: utf-8 -*-
from django import forms
from  .models import  Contact

class ContactForm (forms.ModelForm):
    """Форма обратной связи"""
    class Meta:
        model = Contact
        fields = ['name', 'category', 'email', 'nomer_id', 'message']
