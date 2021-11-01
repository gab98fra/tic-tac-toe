
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('cuenta.urls')),
    path('admin/', admin.site.urls),
    path('juego/', include('juego.urls')),
    
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
