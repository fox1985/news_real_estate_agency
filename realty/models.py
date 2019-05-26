# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Названия категории', unique=True)
    class Meta:
        db_table = 'category'
        verbose_name = u'категория'
        verbose_name_plural = u'Категории'


    def __unicode__(self):
        return u'Категория %s' % self.category_name


class Info(models.Model):
    info_name = models.CharField(max_length=100, verbose_name='Удобства')
    def __unicode__(self):
        return self.info_name

    class Meta:
        db_table = 'info'
        verbose_name = u'Удобства'
        verbose_name_plural = u'Удобства'



class Realty_Page(models.Model):
    author = models.ForeignKey('auth.User', verbose_name='агент')
    realty_name = models.CharField(max_length=200, verbose_name='Название товара',)
    category = models.ForeignKey(Category, verbose_name='категория')
    vid_name = models.CharField(max_length=100, verbose_name='вид', help_text='Вид недвижимости на пример новострой',blank=True)
    tip_name = models.CharField(max_length=100, verbose_name='Тип', help_text='Тип недвижимость',blank=True)
    page_info = models.ManyToManyField(Info, verbose_name='Удобства',help_text='Что есть в доме',blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    sale_and_rental = models.CharField(max_length=100, verbose_name='Для', help_text='Продажа или аренда',blank=True)
    city = models.CharField(max_length=100, verbose_name='Город',blank=True)
    region = models.CharField(max_length=100, verbose_name='Регион',blank=True)
    bedrooms = models.IntegerField(verbose_name='Спальни',default=0)
    rooms = models.IntegerField(verbose_name='Комнат',default=0)
    bathrooms = models.IntegerField(verbose_name='Санузлы',default=0)
    area = models.IntegerField(verbose_name='площадь',default=0)
    land_area = models.IntegerField(verbose_name='площадь участка',default=0)
    from_the_sea = models.IntegerField(verbose_name='от моря',default=0)
    floor = models.IntegerField(verbose_name='Этаж',default=0)
    garash = models.IntegerField(verbose_name='Гараж',default=0)
    room_id = models.IntegerField(verbose_name='Номер ID',default=0,)
    date = models.DateField(auto_now=True,  verbose_name='Дата')
    brief_description = models.TextField(blank=True, verbose_name='Краткое описания',)
    body = models.TextField(blank='True', verbose_name='Полное описания')
    description = models.TextField(max_length=100,verbose_name="Дискрипшин", help_text='Описания для поиска Яндекс и googla слова добавлет через запятую',blank=True)
    keywords = models.TextField(max_length=100,verbose_name="Ключивые слова", help_text='Ключивые слова для поиска Яндекс и googla слова добавлет через запятую',blank=True)

    main_image = models.ImageField(upload_to='main_image/img', verbose_name='Фото на главной страници', blank=True)
    published = models.BooleanField(default=False, verbose_name='Опубликован')  # Чек бокс - опубликован!

    def img(self):
        if self.main_image:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.main_image.url)
        else:
            return '(Нет изображения)'

    img.short_description = 'Картинка Категории'
    img.allow_tags = True


    class Meta:
        db_table = 'realty_page'
        verbose_name = u'Товар'
        verbose_name_plural = u'Товары'



    def __unicode__(self):
        return u'Товар %s' % self.realty_name




class Galary_image(models.Model):
    realty_page = models.ForeignKey(Realty_Page, blank=True, null=True, on_delete=models.CASCADE)
    galary_image = models.ImageField(upload_to='galary/img',verbose_name='Картинка',blank=True)
    class Meta:
        db_table = 'galary_image'
        verbose_name = u'Галирея'
        verbose_name_plural = u'Галиреи'

