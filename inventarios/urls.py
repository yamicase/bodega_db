from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventarios/', include('inventarios.urls')),  # Incluir las URLs de la app inventarios
]
