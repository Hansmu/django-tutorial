"""django_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views
from blogposts import views as blog_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.projects_home, name='home'),  # The first parameter is a regex. $ matches the / landing page.
    url(r'^pig-latin/', views.latin_home, name='latin-home'),
    url(r'^translate/', views.translate, name='url-translate-alias-for-django'),
    url(r'^blog/', blog_views.blog_home, name='blog-home'),
    url(r'^blog/posts/(?P<post_id>[0-9]+)/$', blog_views.post_details, name='post_details')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
