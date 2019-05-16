# -*- coding: utf-8 -*-
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ProcessFormView, FormView
from django.core.urlresolvers import reverse

from realty.models import Category, Realty_Page, Galary_image


from realty.views import CategoryLlistMixin

from  realty.forms import Form_realty_page



class Rrealty_PageEditMixin(CategoryLlistMixin):
    def get_context_data(self, **kwargs):
        context = super(Rrealty_PageEditMixin, self).get_context_data(**kwargs)
        try:
            context["pn"] = self.request.POST["page"]

        except KeyError:
            context["pn"] = "1"
        return context


class  Rrealty_PageEditView(ProcessFormView):
    def post(self, request, *args, **kwargs):
        try:
            pn = request.GET["page"]

        except KeyError:
            pn = "1"
        self.success_url = self.success_url + "?page=" + pn
        return super(Rrealty_PageEditView, self).post(request, *args, **kwargs)


class Form_Galary_View(FormView):
    """Добавления товара через форму"""
    form_class = Form_realty_page
    template_name = 'edit/new_page.html'
    success_url = '/'  # переадресация на страницу в случае успешной отправки

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        galary_image = request.FILES.getlist('galary_image')
        if form.is_valid():
            pk = form.save().pk
            realty_page = Realty_Page.objects.get(pk=pk)
            if galary_image:
                for f in galary_image:
                    fl = Galary_image(realty_page=realty_page, galary_image=f)
                    fl.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class Realty_PageUpdate(UpdateView, Rrealty_PageEditMixin, Rrealty_PageEditView):
    """редактировать товар"""
    model = Realty_Page
    template_name = "edit/edit_page.html"
    pk_url_kwarg = "page_id"
    success_url = '/'

    fields = ['author', 'realty_name', 'category', 'vid_name', 'tip_name', 'page_info', 'price', 'sale_and_rental',

                  'city', 'region', 'bedrooms', 'rooms', 'bathrooms', 'area', 'land_area', 'from_the_sea', 'floor',
                  'room_id',

                  'brief_description', 'body', 'main_image'
                  ]








class Realty_PageDelete(DeleteView, Rrealty_PageEditMixin, Rrealty_PageEditView):
    """Удалиить товары"""
    model = Realty_Page
    template_name = "edit/delete_page.html"
    pk_url_kwarg = "page_id"

    def post(self, request, *args, **kwargs):
        self.success_url = reverse("realty:realty_category_page", kwargs={"cat_id": Realty_Page.objects.get(pk=kwargs["page_id"]).category.id} )
        return super(Realty_PageDelete, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Realty_PageDelete, self).get_context_data(**kwargs)
        return context











