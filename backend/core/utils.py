from django.core.paginator import Paginator
from django.db.models import Count
from django.core.cache import cache

from post.models import Posts
from category.models import Category


class DataMixinPost:

    def get_user_context(self, count, **kwargs):
        context = kwargs
        page = self.request.GET.get('page')
        paginator = Paginator(Posts.objects.all().select_related('user'),
                              count)
        try:
            items = paginator.page(page)
        except Exception:
            items = paginator.page(1)
        context['page_obj'] = items
        return context


class DataMixinCat:

    paginate_by = 21

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = cache.get('cats')
        if not cats:
            cats = Category.objects.annotate(Count('arts'))
            cache.set('cats', cats, 60)

        context['cats'] = cats

        if 'cat_selected' not in context:
            context['cat_selected'] = 0

        return context
