from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/', views.create, name='clone-create-post'),
    url(r'^$', views.homepage, name='clone-homepage'),
    url(r'^(?P<post_id>[0-9]+)/upvote', views.upvote, name='clone-upvote'),
    url(r'^(?P<post_id>[0-9]+)/downvote', views.downvote, name='clone-downvote')
]