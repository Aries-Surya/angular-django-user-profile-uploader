from django.urls import path
from .views import upload_zip

urlpatterns = [
    path('upload/', upload_zip, name='upload-zip'),
]

# filepath: mysite/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
]