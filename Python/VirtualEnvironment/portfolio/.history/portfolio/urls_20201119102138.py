from django.urls import path

from . import views

urlpatterns = [
    pa('', views.index, name='index'),
]