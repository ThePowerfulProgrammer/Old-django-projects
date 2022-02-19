from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.listView, name='list'),
    path('add', views.addMovie, name='add'),
    path('random', views.randomMovie, name='random'),
    path('movies', views.selectMovie, name='movies'),
    path('discover', views.discoverMovie, name='discover'),
    path('popular', views.popularMovie, name='popular'),
]