from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('',views.home),
    path('search/',views.search),
    path('id/<id>/',views.movieDetails,name="movie_details"),
    path('about/',views.about),
    # path('<movie>/reviewed/',include('review.urls')),
    
]

