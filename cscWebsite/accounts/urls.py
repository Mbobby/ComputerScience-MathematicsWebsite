from django.conf.urls import url
from django.conf import settings
from django.contrib.auth import views as auth_views
#from forms import LoginForm
import views

urlpatterns = [
    # url(r'^$', views.login, name='login'),
    #url(r'^login/$', auth_views.login, {'template_name': 'accounts/login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'posts_index'}, name='logout'),
    url(r'^change-password/$', auth_views.password_change, {'post_change_redirect': 'login'}, name='change_password'),
]