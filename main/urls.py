from django.contrib import admin
from django.urls import path
from files import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.about, name="about"),
    path("signup/", views.signup, name="signup"),
    path("details/", views.items, name="details"),
]
