from django.shortcuts import render

from .models import Arts

from post.models import Posts


def arts(request):
    artscards = Arts.objects.all()
    posts = Posts.objects.all()
    return render(request, 'arts/arts.html', {'cards': artscards,
                                              'posts': posts})
