from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),               # Admin site URL
    path('auth/', include('usuarios.urls')),       # URLs for authentication (assuming usuarios.urls handles authentication)
    path('divulgar/', include('divulgar.urls')),   # URLs for divulgar (assuming divulgar.urls handles pet listing and details)
    path('adotar/', include('adotar.urls')),       # URLs for adotar (assuming adotar.urls handles adoption requests)
]

# Serving media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
