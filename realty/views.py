# -*- coding: utf-8 -*-
from news_real_estate_agency import settings
from realty.models import Category, Realty_Page, Galary_image
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import ContextMixin, View
#---------------------------------------------------------------------------------
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from  news_real_estate_agency.emailsettings import EMAIL_HOST_USER
#отправка собщений пользовтелю
from django.contrib import messages






class CategoryLlistMixin(ContextMixin):
    """Выводит меню категории"""
    def get_context_data(self, **kwargs):
        context = super(CategoryLlistMixin, self).get_context_data(**kwargs)
        context["categorys"] = Category.objects.order_by("category_name")
        return context



class Realty_PageListView(ListView, CategoryLlistMixin):
    """Вывод страницы катигории  realty_pages"""
    template_name = "page/realty_category_page.html"
    context_object_name = 'realty_pages'
    queryset = Realty_Page.objects.order_by("realty_name")

    paginate_by = 1
    cat = None

    def get(self, request, *args, **kwargs):
        if self.kwargs["cat_id"] == None:
            'Возвращает первый объект из выборки, ' \
            'или None если ничего не найдено  first() метод'
            self.cat = Category.objects.first()
        else:
            self.cat = Category.objects.get(pk=self.kwargs["cat_id"])

        return super(Realty_PageListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Realty_PageListView, self).get_context_data(**kwargs)
        context['category'] = self.cat
        return context

    def get_queryset(self):
        return Realty_Page.objects.filter(category=self.cat).filter(published=True)




class Realty_PageDetailView(DetailView, CategoryLlistMixin):
    """Класс контролер подключает cat_id катигории """
    template_name = "page/realty_category_page.html"
    model = Realty_Page
    pk_url_kwarg = "cat_id"

    def get_context_data(self, **kwargs):
        context = super(Realty_PageDetailView, self).get_context_data(**kwargs)
        try:
            context["pn"] = self.request.GET["page"]
        except KeyError:
            context["pn"] = "1"
        return context





class Realty_PageDetailView(DetailView, CategoryLlistMixin):
    # Вывод страницы товара и под ключает ID  страницы товара  page_id
    template_name = "page/realty_page_noe.html"
    model = Realty_Page
    pk_url_kwarg = "page_id"


    def get_context_data(self, **kwargs):
        context = super(Realty_PageDetailView, self).get_context_data(**kwargs)
        try:
            context["pn"] = self.request.GET["page"]
        except KeyError:
            context["pn"] = "1"
        return context





class Galary_imageListView(ListView, CategoryLlistMixin):
    """Вывод фото галирею """
    template_name = "page/realty_page_noe.html"
    queryset = Galary_image.objects.all()
    cat = None

    def get(self, request, *args, **kwargs):
        if self.kwargs["cat_id"] == None:
            'Возвращает первый объект из выборки, ' \
            'или None если ничего не найдено  first() метод'
            self.cat = Realty_Page.objects.first()
        else:
            self.cat = Realty_Page.objects.get(pk=self.kwargs["cat_id"])

        return super(Galary_imageListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Galary_imageListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Galary_image.objects.filter(category=self.cat).order_by("galary_image")



class Galary_imageDetailView(DetailView, CategoryLlistMixin):
    # Вывод страницы товара и под ключает ID  страницы товара  page_id
    template_name = "page/realty_page_noe.html"
    model = Galary_image
    pk_url_kwarg = "page_id"

    def get_context_data(self, **kwargs):
        context = super(Galary_imageDetailView, self).get_context_data(**kwargs)
        return context


#---------------------------------------------------------------------------------------------------------------------

# Функция формы обратной связи

def page_contact(request):
    mailfrom = EMAIL_HOST_USER
    mailto = [EMAIL_HOST_USER]
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            name = u'От torrehome.ru  - Новое письмо от {} '.format(cd['name'],)
            message = u'Прислал {}. \n \n \n \n Пишет: {}. \n \n \n  ID номер: {} '.format(cd['email'],  cd['message'], cd['nomer'])
            send_mail(name, message, mailfrom,  mailto,)


    else:
        form = ContactForm()
    return render(request, 'contact/thanks.html')











