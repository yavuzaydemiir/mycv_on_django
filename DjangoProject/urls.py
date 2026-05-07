from django.contrib import admin
from django.urls import path
from django.conf import settings  # Bunu ekle
from django.conf.urls.static import static  # Bunu ekle
from myCV.views import index, contact  # Kendi view isimlerin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)