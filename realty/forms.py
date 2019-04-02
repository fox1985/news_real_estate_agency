# -*- coding: utf-8 -*-
from realty.models import Category,  Realty_Page, Galary_image

from django import forms







class Form_realty_page(forms.ModelForm):

    class Meta:
        model = Realty_Page
        fields = ['author', 'realty_name', 'category', 'vid_name', 'tip_name', 'page_info', 'price', 'sale_and_rental',

                  'city', 'region', 'bedrooms', 'rooms', 'bathrooms', 'area', 'land_area', 'from_the_sea', 'floor',
                  'room_id',

                  'brief_description', 'body', 'main_image'



                  ]



        labels = {
            'author': 'Агент',
            'realty_name' : 'Название товара',

            'category'  : 'Выберите категорию',
            'vid_name' : 'вид',

            'tip_name': 'Тип',

            'page_info' : 'Удобства',

            'price' : 'Цена',

            'sale_and_rental' : 'Для',

            'city' : 'Город',

            'region' : 'Регион',

            'bathrooms' : 'Спальни',

            'rooms' : 'Комнат',

            'bathrooms' : 'Санузлы',

            'area' : 'площадь',

            'land_area' : 'площадь',

            'from_the_sea' : 'от моря',

            'floor' : 'Этаж',

            'room_id' : 'Номер ID',

            'brief_description' : 'Краткое описания',

            'body' : 'Полное описания',

            'main_image' : 'Фото на главной страници',

        }

        help_texts = {"vid_name": "Вид пример новострой",

                      'tip_name': 'Тип недвижимость',

                      'sale_and_rental' : 'Продажа или аренда',

                      'land_area': 'участка',


                      }



class Form_Galary_image(forms.ModelForm):

    class Meta:
        model = Galary_image

        fields = ['galary_image']

        labels = {
            'galary_image': 'Загрузка фото',
        }


