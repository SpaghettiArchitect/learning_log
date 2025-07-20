"""Defines URL patterns for accounts."""

from django.urls import include, path

app_name = "accounts"
urlpatterns = [
    # Include default auth urls.
    path("", include("django.contrib.auth.urls")),
]
