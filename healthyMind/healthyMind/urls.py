from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('principal.urls')),
    path('e-books/', include('shop.urls')),
    path('contact/', include('contact.urls')),
    path('registro/', include('registro.urls'))
]

#Servir los ficheros medias en modo DEBUG
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
