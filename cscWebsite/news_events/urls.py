from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='news_events_index'),
    url(r'^news/(?P<news_id>[0-9]+)/$', views.news_detail, name='news_detail'),
    url(r'^events/(?P<event_id>[0-9]+)/$', views.events_detail, name='events_detail'),
    url(r'^news/$', views.news_index, name='news_index'),
    url(r'^events/$', views.events_index, name='events_index'),
]