# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
  if request.method == 'POST':
    page_id = request.POST['page_id']
    listing = request.POST['listing']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    realtor_email = request.POST['realtor_email']

    #  Check if user has made inquiry already
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(page_id=page_id, user_id=user_id)
      if has_contacted:
        messages.error(request, 'Вы уже сделали запрос для этого списка')
        return redirect('/realty/'+page_id)

    contact = Contact(listing=listing, page_id=page_id, name=name, email=email, phone=phone, message=message, user_id=user_id )

    contact.save()

    # Send email
    # send_mail(
    #   'Property Listing Inquiry',
    #   'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
    #   'traversy.brad@gmail.com',
    #   [realtor_email, 'techguyinfo@gmail.com'],
    #   fail_silently=False
    # )

    messages.success(request, 'Ваш запрос был отправлен, агент по продаже недвижимости свяжется с вами в ближайшее время')
    return redirect('/realty/'+page_id)
