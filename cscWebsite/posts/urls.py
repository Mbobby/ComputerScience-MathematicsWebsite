from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='posts_index'),
    url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='posts_detail'),
]