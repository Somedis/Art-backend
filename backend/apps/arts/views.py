from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Arts

from post.models import Posts


def arts(request):
    artscards = Arts.objects.all()
    posts = Posts.objects.all()

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'arts/arts.html', {'cards': artscards,
                                              'page_obj': page_obj})


def show_art(request, art_slug):
    posts = Posts.objects.all()
    art = get_object_or_404(Arts, slug=art_slug)

    context = {
        'posts': posts,
        'art': art,
    }

    return render(request, 'arts/show_art.html', context=context)
