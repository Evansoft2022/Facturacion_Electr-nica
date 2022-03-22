from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('home.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^list_data/', include('list_data.urls')),
    # url(r'^data/', include('data.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)