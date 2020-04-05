from django.conf.urls import  url
from . import views

urlpatterns = [
    url('', views.FeedBackView.as_view(), name='contact'),

]