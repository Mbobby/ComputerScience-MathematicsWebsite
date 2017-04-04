from django.shortcuts import render, redirect
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


from models import Post
from forms import PostForm

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

@login_required
def my_posts(request):
	posts = Post.objects.filter(created_by=request.user.id)
	context = {"posts": posts}
	return render(request, "posts/my_posts.html", context)

@login_required
def create(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post_form = form.save(commit=False)
			post_form.created_by = request.user
			post_form.save()
			return redirect("posts_index")
		else:
			print "Invalid Form"
			return redirect("posts_index")
	context = {"form":PostForm}
	return render(request, "posts/create.html", context)

@login_required
def edit(request, post_id):
	if request.method == "POST":
		post = Post.objects.get(id=post_id)
		post_form = PostForm(request.POST or None, instance=post)
		if post_form.is_valid():
			post_form.save()
			return redirect("my_posts")
	post = Post.objects.get(id=post_id)
	post_form = PostForm(request.POST or None, instance=post)
	context = {"form": post_form, "post": post}
	return render(request, "posts/edit.html", context)