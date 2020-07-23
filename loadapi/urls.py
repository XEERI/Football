from django.urls import path

from . import views
# from . views import SearchList

app_name = 'loadapi'

urlpatterns = [
path('', views.index),
# path('sendrequestplayer', views.sendPlayer),
# path('sendrequestmatch', views.sendMatch),
path('importplayer', views.importplayer),
path('importmatch', views.importmatch),


]