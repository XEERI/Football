from django.contrib import admin
from django.urls import path
from . import views

app_name = 'footballstats'
urlpatterns = [

    path('', views.get_player_data, name='player_data'),
    path('players/', views.get_player_data, name='player_data'),
    # path('players/<int:player_key>', views.player_details, name='player_details'),
    path('match', views.get_match_data, name='match_data'),
    path('matches/', views.get_match_data, name='match_data'),
    path('matches/<int:match_id>', views.match_details, name='match_details'),
]