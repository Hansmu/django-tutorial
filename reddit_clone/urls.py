from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/', views.create, name='clone-create-post'),
    url(r'^$', views.homepage, name='clone-homepage')
]