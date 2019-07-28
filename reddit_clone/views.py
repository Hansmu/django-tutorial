from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from reddit_clone.models import Post


@login_required
def create(request):
    error = ''

    if request.method == 'POST':
        if request.POST['title'] and request.POST['url']:
            post = Post()

            post.title = request.POST['title']
            post.url = request.POST['url']
            post.published_date = timezone.datetime.now()
            post.author = request.user

            post.save()

            return redirect('clone-homepage')
        else:
            error = 'You must include a title and URL to create a post!'

    return render(request, 'reddit/create-post.html', {'error': error})


def homepage(request):
    posts = Post.objects.order_by('score')
    return render(request, 'reddit/homepage.html', {'posts': posts})


def upvote(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(pk=post_id)
        post.score += 1
        post.save()
        return redirect('clone-homepage')


def downvote(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(pk=post_id)
        post.score -= 1
        post.save()
        return redirect('clone-homepage')
