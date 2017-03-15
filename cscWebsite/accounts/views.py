from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import views as auth_views
from forms import LoginForm
# Create your views here.

def login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	return auth_views.login(request, template_name= 'accounts/login.html',authentication_form=LoginForm)
