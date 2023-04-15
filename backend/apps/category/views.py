from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Category

from .forms import AddCategoryForm

from post.models import Posts


def categories(request):
    cats = Category.objects.all()
    posts = Posts.objects.all()

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'category/categories.html', {'cats': cats,
                                                        'page_obj': page_obj})


def show_category(request, cats_slug):
    posts = Posts.objects.all()
    cat = get_object_or_404(Category, slug=cats_slug)

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'cat': cat,
        'page_obj': page_obj,
    }

    return render(request, 'category/show_category.html', context=context)


class AddCategoryView(CreateView):

    form_class = AddCategoryForm
    template_name = 'category/add_category.html'
    success_url = reverse_lazy('cats')
