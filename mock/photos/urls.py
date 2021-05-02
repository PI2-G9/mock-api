from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_photos_and_users, name='index'),
]