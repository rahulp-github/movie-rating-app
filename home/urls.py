from django.urls import path
from django.urls.conf import include
from . import views
from top_charts import views as top_chart_view

urlpatterns = [
    path('',views.home),
    path('search/',views.search),
    path('id/<id>/',views.movieDetails,name="movie_details"),
    path('about/',views.about),
    path('top/',include('top_charts.urls')),
    path('topBoxOffice/',top_chart_view.top_box_office,name='topBoxOffice'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.user_logout,name='logout'),
    path('watchlist/<id>/<movie_name>/<year>',views.watch_list,name='watchlist'),
    path('yourWatchlist/',include('watchlist.urls')),
]

