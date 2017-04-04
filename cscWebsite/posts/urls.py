from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='posts_index'),
    url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='posts_detail'),
    url(r'^create/$', views.create, name='create_post'),
    url(r'^my_posts/$', views.my_posts, name='my_posts'),
    url(r'^edit/(?P<post_id>[0-9]+)/$', views.edit, name='edit_post'),
]