from django.shortcuts import render
# from django.views.generic.base import TemplateView
from django.utils import timezone
from django.views.generic import DetailView, ListView, View

from .models import PreviewImage


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
    return render(request, 'home/index.html', {'homepage': homepage, })
