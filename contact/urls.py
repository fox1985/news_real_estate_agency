
from django.conf.urls import  url
from  contact.views import contactform


urlpatterns = [
    url(r'^$', contactform, name='contact'),

]