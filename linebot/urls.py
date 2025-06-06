from django.contrib import admin
from django.urls import path, include   # Add


urlpatterns = [
    path('bot_app/', include('bot_app.urls')),   # Add
    path('admin/', admin.site.urls),
]
