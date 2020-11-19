from django.urls import url

from . import views

urlpatterns = [
    o('', views.index, name='index'),
]