"""cscWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from .views import index as home

urlpatterns = [
	url(r'^posts/', include('posts.urls')),
    url(r'^news_events/', include('news_events.urls')),
    url(r'^faculty/', include('faculty.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),

    #Contingencies
    url(r'^login/$', RedirectView.as_view(url='/accounts/login')),
    url(r'^logout/$', RedirectView.as_view(url='/accounts/logout')),

    #Link to HomePage, implemented in cscWebsite
    url(r'^$', home, name="home"),
]
