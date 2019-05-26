
from django.conf.urls import  url
from  contact.views import page_contact


urlpatterns = [
    url(r'^contact/', page_contact, name='contact'),



]