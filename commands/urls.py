from django.urls import path

from . import views

app_name = 'commands'

urlpatterns = [
    path('', views.home, name="home"),
    path('commands/search/', views.search, name="search"),
    path('commands/language/<int:language_id>/',
         views.language, name="language"),
    path('commands/<int:id>/', views.command, name="command"),
]
