from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include, url

urlpatterns = [
    path("admin/", admin.site.urls),
    url(r"^", include("credit_cards.urls")),
]
