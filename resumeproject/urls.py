from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('services/', include('services.urls')),
    path('skills', include('edu.urls')),
]
