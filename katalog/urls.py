from django.urls import path
from . import views


urlpatterns = [
    path('', views.katalog_home, name='katalog_home'),
]