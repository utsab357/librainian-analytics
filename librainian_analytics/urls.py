from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # API urls
    path("api/analytics/", include("analytics.urls")),
]
