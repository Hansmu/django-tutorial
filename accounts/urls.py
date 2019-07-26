from django.conf.urls import url
from . import views

# If you have a lot of similar named URLs, then it could be helpful to add a prefix
app_name = 'accounts'

urlpatterns = [
    url(r'^signup/', views.signup, name='clone-signup'),
    url(r'^login/', views.user_login, name='clone-login')
]