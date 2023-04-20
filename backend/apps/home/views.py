from django.views.generic import ListView

from .models import PreviewImage

from core.utils import DataMixinPost


class HomePageView(DataMixinPost, ListView):

    model = PreviewImage
    template_name = 'home/index.html'
    context_object_name = 'homepage'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(count=3)
        context['count'] = range(0, self.model.objects.count())
        return dict(list(context.items()) + list(c_def.items()))
