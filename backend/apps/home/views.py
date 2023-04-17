from django.core.paginator import Paginator
from django.views.generic import ListView

from .models import PreviewImage

from post.models import Posts


class HomePageView(ListView):

    model = PreviewImage
    template_name = 'home/index.html'
    context_object_name = 'homepage'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page')
        paginator = Paginator(Posts.objects.all(), 3)
        try:
            items = paginator.page(page)
        except Exception:
            items = paginator.page(1)
        context['page_obj'] = items
        context['count'] = range(0, PreviewImage.objects.all().__len__())
        return context
