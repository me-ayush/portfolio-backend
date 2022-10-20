from django.urls import path

from . import views

urlpatterns = [
    path("certificates", views.certificates, name="certificates")
]