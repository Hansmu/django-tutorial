from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^posts/(?P<post_id>[0-9]+)/$', views.post_details, name='post_details'),
    url(r'^$', views.blog_home, name='blog-home')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
