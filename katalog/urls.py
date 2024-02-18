from django.urls import path
from . import views


urlpatterns = [
    path('', views.katalog_home, name='katalog_home'),
    path('create', views.create, name='create'),
    path('<int:pk>/update', views.KatalogUpdateView.as_view(), name='katalog-update'),
    path('<int:pk>/delete', views.KatalogDeleteView.as_view(), name='katalog-delete')
]