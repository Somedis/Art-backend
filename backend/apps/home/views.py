from django.shortcuts import render
from django.core.paginator import Paginator
# from django.views.generic.base import TemplateView
from django.utils import timezone # noqa
from django.views.generic import DetailView, ListView, View # noqa

from .models import PreviewImage

from post.models import Posts


# class HomePageView(ListView):

#     template_name = 'home/index.html'
#     model = PreviewImage
#     context_object_name = 'preview'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['home'] = PreviewImage.objects.all()
#         print(context)
#         return context

def index(request):
    homepage = PreviewImage.objects.all()
    posts = Posts.objects.all()
    count = range(0, homepage.__len__())

    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home/index.html', {'homepage': homepage,
                                               'count': count,
                                               'page_obj': page_obj})
