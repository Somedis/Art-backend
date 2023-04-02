from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from config.settings import base

from home.views import index
from arts.views import arts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('arts/', arts, name='arts'),
]

if base.DEBUG:

    urlpatterns += static(base.MEDIA_URL,
                          document_root=base.MEDIA_ROOT)
