from django.shortcuts import render, get_object_or_404
from .models import Blog, Header
from django.http import HttpResponse, HttpResponseRedirect

from .form import PostModelForm


def create_post(request):
    # if request.method == 'POST':
    #     form = PostModelForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit=False)
    #         print(form.cleaned_data)
    form = PostModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect('/blog/{num}'.format(num=obj.id))
    context = {
        'form': form
    }

    return render(request, 'blog/create.html', context)


def allblogs(request):
    qs = Blog.objects.all().order_by('-id')[:2]
    he = get_object_or_404(Header, id=1)
    context = {
        'title': 'Это блог',
        'he': he,
        'blogs': qs,

    }

    return render(request, 'blog/home.html', context)


def detail(request, id):
    detail = get_object_or_404(Blog, id=id)
    he = get_object_or_404(Header, id=1)

    return render(request, 'blog/detail.html', {'blog': detail, 'he': he})
