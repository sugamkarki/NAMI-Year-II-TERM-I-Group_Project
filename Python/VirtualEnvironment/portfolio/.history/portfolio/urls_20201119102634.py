from django.urls import path

from . import views

urlpatterns = [
    path('don/', views.index, name='index'),
    path('cat/',views.cat)
]