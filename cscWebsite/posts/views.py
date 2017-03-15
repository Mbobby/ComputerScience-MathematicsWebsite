from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#from django.contrib.auth.decorators import login_required

from models import Post

# Create your views here.

#@login_required(login_url='login')


def index(request):
	posts = Post.objects.filter(is_published=True)

	paginator = Paginator(posts, 10) # Show 10 posts per page
	page = request.GET.get("page")

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		posts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		posts = paginator.page(paginator.num_pages)
	context = {'posts': posts}
	return render(request, "posts/index.html", context)

def detail(request, post_id):
	try:
		post = Post.objects.get(id=post_id)
		if post.is_published == False:
			raise Http404("The post does not exist")
	except Post.DoesNotExist:
		raise Http404("The post does not exist")
	context = {"post": post}
	return render(request, "posts/detail.html", context)