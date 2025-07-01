from django.contrib import admin
from django.urls import path, include   # Add
from bot_app.views import upload_picture

urlpatterns = [
    path('bot_app/', include('bot_app.urls')),   # Add
    path('admin/', admin.site.urls),
]
