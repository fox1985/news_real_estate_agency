# -*- coding: utf-8 -*-
from django.views.generic import FormView

from realty.models import Category, Realty_Page, Galary_image
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import ContextMixin

class CategoryLlistMixin(ContextMixin):
    """Выводит меню категории"""
    def get_context_data(self, **kwargs):
        context = super(CategoryLlistMixin, self).get_context_data(**kwargs)
        context["categorys"] = Category.objects.order_by("category_name")
        return context


class Realty_PageListView(ListView, CategoryLlistMixin):
    """Вывод страницы катигории  realty_pages"""
    template_name = "realty_category_page.html"
    context_object_name = 'realty_pages'
    queryset = Realty_Page.objects.order_by("realty_name")

    paginate_by = 10
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
        return Realty_Page.objects.filter(category=self.cat).order_by("realty_name")




class Realty_PageDetailView(DetailView, CategoryLlistMixin):
    """Класс контролер подключает cat_id катигории """
    template_name = "realty_category_page.html"
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
    # Вывод страницы товара и под ключает ID  страницы товара  one_pagi_id
    template_name = "realty_page_noe.html"
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
    template_name = "realty_page_noe.html"
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
    # Вывод страницы товара и под ключает ID  страницы товара  one_pagi_id
    template_name = "realty_page_noe.html"
    model = Galary_image
    pk_url_kwarg = "page_id"

    def get_context_data(self, **kwargs):
        context = super(Galary_imageDetailView, self).get_context_data(**kwargs)
        return context
