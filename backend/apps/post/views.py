from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .forms import PostForm


class AddPostView(CreateView):

    form_class = PostForm
    template_name = 'posts/add_post.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = User.objects.get(username=self.request.user)
        return super(AddPostView, self).form_valid(form)
