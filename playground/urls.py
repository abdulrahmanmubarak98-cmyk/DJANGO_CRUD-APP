from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.create_note),
    path("hello/", views.create_note, name="home"),
    path("edit/<int:note_id>/", views.edit_note, name="edit_note"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout_view, name="logout"),
    path("delete/<int:note_id>/", views.delete_note, name="delete_note"),
]
