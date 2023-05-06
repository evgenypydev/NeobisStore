from django.contrib import admin
from django.urls import path, include, re_path
from djoser import urls

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path('auth/', include('djoser.urls')),
    re_path('auth/', include('djoser.urls.authtoken')),
    re_path('auth/', include('djoser.urls.jwt')),
]
