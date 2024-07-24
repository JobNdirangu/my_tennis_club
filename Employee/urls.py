from django.urls import path
from.import views

urlpatterns = [
    # path('home/', views.home,name="home"),
    path('dashboard/', views.dashboard,name="dashboard"),

    path('saveemployee/', views.saveemployee,name="saveemployee"),
    path('employees/', views.employees,name="employees"),
    path('delete_emp/<int:employee_id>', views.delete_emp,name="delete_emp"),
    path('update_emp/<int:employee_id>', views.update_emp,name="update_emp"),

    path('playerview/', views.playerview,name="playerview"),
    path('delete_player/<int:player_id>', views.delete_player,name="delete_player"),
    path('update_player/<int:player_id>', views.update_player,name="update_player"), 
    path('playeradd/', views.addplayer,name="playeradd"),  

    path('kitview/', views.kitview,name="kitview"),
    path('delete_kit/<int:kit_id>', views.delete_kit,name="delete_kit"),
    path('update_kit/<int:kit_id>', views.update_kit,name="update_kit"), 
    path('kitadd/', views.addkit,name="kitadd"), 
]
