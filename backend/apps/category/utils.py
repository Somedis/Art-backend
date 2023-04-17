from django.core.paginator import Paginator

from post.models import Posts


class DataMixin():

    def get_user_context(self, **kwargs):
        context = kwargs
        page = self.request.GET.get('page')
        paginator = Paginator(Posts.objects.all(), 5)
        try:
            items = paginator.page(page)
        except Exception:
            items = paginator.page(1)
        context['page_obj'] = items
        return context
