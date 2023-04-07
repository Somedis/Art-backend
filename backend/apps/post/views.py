from django.shortcuts import redirect, render
# from django.views.generic import CreateView
# from django.urls import reverse_lazy

from .forms import PostForm


def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            form.save_m2m()
            return redirect('home')

    form = PostForm()
    context = {
        'form': form
    }

    return render(request, 'posts/add_post.html', context=context)


# class PostView(CreateView):

#     form_class = PostForm
#     template_name = 'posts/add_post.html'
#     success_url = reverse_lazy('home')
