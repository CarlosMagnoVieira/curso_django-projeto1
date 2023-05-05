from django.urls import path

#from commands.views import home

from . import views


urlpatterns = [
    path('', views.home),
    path('commands/<int:id>/', views.command),
]