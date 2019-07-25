from django.shortcuts import render
from . import models


def blog_home(request):
    posts = models.Post.objects.order_by('published_date')
    return render(request, 'posts/blog-home.html', {
        'posts': posts
    })
