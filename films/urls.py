from django.urls import path
from films.views import *

urlpatterns = [
    path('', FilmsView.as_view(), name='home_page_url'),
    path('search/', SearchView.as_view(), name='search_films_url'),
    path('<int:pk>/', FilmView.as_view(), name='film_detail_url'),

]