from django.urls import path

from commands.views import home


urlpatterns = [
    path('', home),
]