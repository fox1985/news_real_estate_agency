# -*- coding: utf-8 -*-
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ProcessFormView, FormView
from django.core.urlresolvers import reverse

from realty.models import Category, Realty_Page, Galary_image


from realty.views import CategoryLlistMixin

from  realty.forms import Form_realty_page, Form_Galary_image



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
        
        




class Realty_PageCreate(CreateView, Rrealty_PageEditMixin):
    model = Realty_Page
    template_name = "edit/new_page.html"

    fields = ['author', 'realty_name', 'category', 'vid_name', 'tip_name', 'page_info', 'price', 'sale_and_rental',

              'city', 'region', 'bedrooms', 'rooms', 'bathrooms', 'area', 'land_area', 'from_the_sea', 'floor',
              'room_id',

              'brief_description', 'body', 'main_image'
              ]


    def get(self, request, *args, **kwargs):
        if self.kwargs["cat_id"] != None:
            self.initial["category"] = Category.objects.get(pk=self.kwargs["cat_id"])
        return super(Realty_PageCreate, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.success_url = reverse('realty:realty_category_page', kwargs={'cat_id': Category.objects.get(pk=self.kwargs['cat_id']).id})
        return super(Realty_PageCreate, self).post(request, *args, **kwargs)



    def get_context_data(self, **kwargs):
        context = super(Realty_PageCreate, self).get_context_data(**kwargs)
        context["category"] = Category.objects.get(pk=self.kwargs["cat_id"])
        return context





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





def dva_form(request, cat_id):
    if request.merhod == 'POST':
        realty_form = Form_realty_page(request.POST, request.FILES)
        galery_form = Form_Galary_image(request.POST, request.FILES)

        if realty_form.is_valid() and galery_form.is_valid():
            realty = realty_form.save()

            gallery = galery_form.save(commit=False)
            realty.realty_page_id = realty.id
            gallery.galery_form.save()
            return  HttpResponseRedirect('/')

        else:
            context = {
                'realty_form': realty_form,
                'galery_form': galery_form,

            }

    else:
        context = {
            'realty_form': Form_realty_page(),
            'galery_form': Form_Galary_image(),

        }
    return TemplateResponse(request, 'edit/new_page.html', context)









