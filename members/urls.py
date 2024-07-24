
from django.urls import path
from.import views

urlpatterns = [
    path('', views.home,name="home"),
    path('players', views.players,name="players"),
    path('fixture', views.fixture,name="fixture"),
    path('gallery', views.gallery,name="gallery"),
    
]
