from django.views.generic import ListView, DetailView

from core.utils import DataMixinCat

from .models import Arts


class ArtsView(DataMixinCat, ListView):

    model = Arts
    template_name = 'arts/arts.html'
    context_object_name = 'arts'

    def get_queryset(self):
        return Arts.objects.filter(is_publish=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class ShowCategoryView(DataMixinCat, ListView):

    model = Arts
    template_name = 'arts/arts.html'
    context_object_name = 'arts'
    allow_empty = False

    def get_queryset(self):
        return Arts.objects.filter(cat__slug=self.kwargs['cat_slug'],
                                   is_publish=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(cat_selected=context['arts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))


class ShowArtView(DataMixinCat, DetailView):

    model = Arts
    template_name = 'arts/show_art.html'
    slug_url_kwarg = 'art_slug'
    context_object_name = 'art'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))
