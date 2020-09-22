from django.urls import path, include
from .views import test

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('test', test),
]

