# -*- coding: utf-8 -*-
"""""
    url(r'^(?:(?P<cat_id>\d+)/)?$', Realty_PageListView.as_view(), name='realty_category_page'),# Выборка категорий

    url(r'^page/?(?P<one_pagi_id>\d+)/$', Realty_PageDetailView.as_view(), name='realty_page_noe'),#выводит  стараницу
"""""


from django.conf.urls import  url
from realty.views import  Realty_PageListView, Realty_PageDetailView, Galary_imageDetailView, Galary_imageListView

from realty.edit import Realty_PageCreate, Realty_PageUpdate, Realty_PageDelete, Form_Galary_View








urlpatterns = [



    url(r'^realty/(?:(?P<cat_id>\d+)/)?$', Realty_PageListView.as_view(), name='realty_category_page' ),# Выборка категорий


    url(r'^page/(?:(?P<page_id>\d+)/)?$', Realty_PageDetailView.as_view(), name='realty_page_noe'),# выводит  стараницу

#-------------------------------------------------------------------------------------------------------------------------------------------
    url(r'^page/(?:(?P<cat_id>\d+)/)?$', Galary_imageListView.as_view(), name='realty_page_noe'),# Вывод фото галирею фильтация галиреи

    url(r'^page/(?:(?P<page_id>\d+)/)?$', Galary_imageDetailView.as_view(), name='realty_page_noe'),# Пдключить ID фотогалиреи








#-----------------------------------------------------------------------------------------------------------------------------------------
    url(r'^add/$', Form_Galary_View.as_view(), name="new_page"),# Добавить товар


    url(r'^page/(?P<page_id>\d+)/edit/$', Realty_PageUpdate.as_view(), name='edit_page'),# редактировать товар

    url(r'^page/(?P<page_id>\d+)/delete/$', Realty_PageDelete.as_view(), name='delete_page'),# удалить товар


    url(r'^(?:(?P<cat_id>\d+)/)?$', Realty_PageListView.as_view(), name='realty_category_page' ),# товар выводит на главную страницу
#------------------------------------------------------------------------------------------------------------------------------------------








]

from django.conf import settings
from django.conf.urls.static import static

# Чтобы показывалась изображения на локальном сервери
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)