from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from config.settings import base

from home.views import index
from arts.views import arts
from users.views import registration, logout_user, login_user
from article.views import AddArticleView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('arts/', arts, name='arts'),
    path('registration/', registration, name='registration'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('addArt/', AddArticleView.as_view(), name='addArt'),
]

if base.DEBUG:

    urlpatterns += static(base.MEDIA_URL,
                          document_root=base.MEDIA_ROOT)
