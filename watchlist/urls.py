from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('',views.your_watchlist,name='your_watchlist'),
    path('delrecord/<id>/',views.delrecord,name='delrecord'),
]