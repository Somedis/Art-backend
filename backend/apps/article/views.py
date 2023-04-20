from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import AddArticleForm


class AddArticleView(CreateView):

    form_class = AddArticleForm
    template_name = 'article/add_art.html'
    success_url = reverse_lazy('arts')
