# -*- coding: utf-8 -*-

"""news_real_estate_agency URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin




urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^realty/', include('realty.urls', namespace='realty')),

    # будем подключать urls.py приложения contact
    url(r'^', include('contact.urls', namespace='contact')),


]



from django.conf import settings
from django.conf.urls.static import static

# Чтобы показывалась изображения на локальном сервери
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)