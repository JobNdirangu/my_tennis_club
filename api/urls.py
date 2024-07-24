from django.urls import path
from.import views

urlpatterns = [
    path('players/', views.PlayerListCreate.as_view(),name="players-list"),
    path('players/<int:pk>', views.PlayerRetrieveUpdateDestory.as_view(), name="players-all")
]