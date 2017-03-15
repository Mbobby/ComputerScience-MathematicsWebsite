from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='faculty_index'),
    url(r'^(?P<faculty_id>[0-9]+)/$', views.detail, name='faculty_detail'),
]