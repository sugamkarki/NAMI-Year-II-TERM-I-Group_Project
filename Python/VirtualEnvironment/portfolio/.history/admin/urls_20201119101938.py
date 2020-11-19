
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('sugam/', include('polls.urls')),
    path('admin/', admin.site.urls),
]