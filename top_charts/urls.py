from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns =[
     
     path('top250ratedmovies/',views.top250,name='top250'),
     path('top10indian/',views.top10,name='top10'),
]