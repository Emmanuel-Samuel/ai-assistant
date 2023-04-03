# import libraries
from django.urls import path
# from current dir, import views
from . import views


# variable for storing app urls
urlpatterns = [
    path('', views.index, name='index'),
    path('getresponse', views.getresponse, name='getresponse'),
    path('getweather', views.getweather, name='getweather'),
    path('getnews', views.getnews, name='getnews')

] 