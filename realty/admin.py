# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from realty.models import Realty_Page, Info,  Category, Galary_image


from django.contrib import admin

# Register your models here.

class Galary_image_Admin(admin.StackedInline):
    model = Galary_image
    extra = 4





class Realty_Page_Admin(admin.ModelAdmin):
    inlines = [Galary_image_Admin]
    list_display = ['realty_name', 'img']
    list_filter = ['date', 'category', 'room_id','price']
    search_fields = ['realty_name']




# Register your models here.
admin.site.register(Info)
admin.site.register(Category)
admin.site.register(Realty_Page, Realty_Page_Admin)



