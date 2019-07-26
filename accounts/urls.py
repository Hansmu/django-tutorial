from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^signup/', views.signup, name='clone-signup'),
    url(r'^login/', views.user_login, name='clone-login')
]