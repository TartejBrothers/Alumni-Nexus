from django.contrib import admin
from django.urls import path
from files import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.about, name="about"),
    path("signup/", views.signup, name="signup"),
    path("details/", views.items, name="details"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
