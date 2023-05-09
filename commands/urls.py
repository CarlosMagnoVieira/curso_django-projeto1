from django.urls import path

#from commands.views import home

from . import views

app_name= 'commands'

urlpatterns = [
    path('', views.home, name="home"),
    path('commands/<int:id>/', views.command, name="command"),
]