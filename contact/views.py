# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.views.generic import View
from .forms import ContactForm
from .models import Contact



class FeedBackView(View):
  def post(self,request):
    form = ContactForm(request.POST)
    if form.is_valid():
      form.save()
    return  redirect('/realty/')

