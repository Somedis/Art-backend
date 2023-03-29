from django.shortcuts import render
from django.views.generic.base import TemplateView

from .models import PreviewImage


class HomePageView(TemplateView):

    template_name = 'templates/home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = PreviewImage.objects.all()
        return context
