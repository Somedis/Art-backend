from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from config.settings import base

from home.views import index
from arts.views import ArtsView, ShowCategoryView, ShowArtView
from users.views import registration, logout_user, login_user
from article.views import AddArticleView
from post.views import add_post
from category.views import categories, show_category, AddCategoryView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('arts/', ArtsView.as_view(), name='arts'),
    path('category/<slug:cat_slug>/', ShowCategoryView.as_view(),
         name='category'),
    path('registration/', registration, name='registration'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('addArt/', AddArticleView.as_view(), name='addArt'),
    path('addPost/', add_post, name='addPost'),
    path('art/<slug:art_slug>/', ShowArtView.as_view(), name='art'),
    path('categories/', categories, name='cats'),
    path('cat/<slug:cats_slug>/', show_category, name='cat'),
    path('addCat/', AddCategoryView.as_view(), name='addCat'),
]

if base.DEBUG:

    urlpatterns += static(base.MEDIA_URL,
                          document_root=base.MEDIA_ROOT)
