from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from config.settings import base

from home.views import HomePageView
from arts.views import ArtsView, ShowCategoryView, ShowArtView
from users.views import registration, login_user, logout_user
from article.views import AddArticleView
from post.views import AddPostView
from category.views import AddCategoryView, CategoriesView, CategoryView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('arts/', ArtsView.as_view(), name='arts'),
    path('category/<slug:cat_slug>/', ShowCategoryView.as_view(),
         name='category'),
    path('registration/', registration, name='registration'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('addArt/', AddArticleView.as_view(), name='addArt'),
    path('addPost/', AddPostView.as_view(), name='addPost'),
    path('art/<slug:art_slug>/', ShowArtView.as_view(), name='art'),
    path('categories/', CategoriesView.as_view(), name='cats'),
    path('cat/<slug:cats_slug>/', CategoryView.as_view(), name='cat'),
    path('addCat/', AddCategoryView.as_view(), name='addCat'),
]

if base.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(base.MEDIA_URL,
                          document_root=base.MEDIA_ROOT)
    urlpatterns += static(base.STATIC_URL,
                          document_root=base.STATIC_ROOT)
