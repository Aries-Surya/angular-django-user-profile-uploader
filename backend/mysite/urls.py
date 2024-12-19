from django.contrib import admin
from django.urls import path, include
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/upload/', views.upload_profile_photos, name='upload_profile_photos'),
    path('', views.index, name='index'),  # Add this line
]