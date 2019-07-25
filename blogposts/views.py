from django.shortcuts import render, get_object_or_404
from . import models


def blog_home(request):
    posts = models.Post.objects.order_by('-published_date')
    return render(request, 'posts/blog-home.html', {
        'posts': posts
    })


def post_details(request, post_id):
    # post = models.Post.objects.get(pk=post_id)
    post = get_object_or_404(models.Post, pk=post_id)
    return render(request, 'posts/post_details.html', {
        'post': post
    })
