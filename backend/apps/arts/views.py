from django.shortcuts import render

from .models import Arts


def arts(request):
    artscards = Arts.objects.all()
    return render(request, 'arts/arts.html', {'cards': artscards, })
