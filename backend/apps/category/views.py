from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from .models import Category

from .forms import AddCategoryForm

from core.utils import DataMixinPost


class CategoriesView(DataMixinPost, ListView):

    model = Category
    template_name = 'category/categories.html'
    context_object_name = 'cats'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(count=5)
        return dict(list(context.items()) + list(c_def.items()))


class CategoryView(DataMixinPost, DetailView):

    model = Category
    template_name = 'category/show_category.html'
    slug_url_kwarg = 'cats_slug'
    context_object_name = 'cat'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(count=5)
        return dict(list(context.items()) + list(c_def.items()))


class AddCategoryView(CreateView):

    form_class = AddCategoryForm
    template_name = 'category/add_category.html'
    success_url = reverse_lazy('cats')
