from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from config.settings import base

from home.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
]

if base.DEBUG:

    urlpatterns += static(base.MEDIA_URL,
                          document_root=base.MEDIA_ROOT)
