from django.urls import path
from dashboard import views

urlpatterns = [
    path("", views.weather_view, name="weather"),
]
