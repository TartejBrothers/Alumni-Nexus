from django.contrib import admin
from django.urls import path
from files import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.about, name="about"),
    path("signup/", views.signup, name="signup"),
    path("details/", views.items, name="details"),
    path("news/", views.news, name="news"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
