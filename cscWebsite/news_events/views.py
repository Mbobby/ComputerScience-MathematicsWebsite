from django.shortcuts import render
from models import Events, News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def index(request):
	events = Events.objects.order_by('event_date')[:3]
	news = News.objects.order_by('-pub_date')[:3]
	context = {"news": news, "events": events}
	return render(request, "news_events/index.html", context)


def events_index(request):
	events = Events.objects.order_by('event_date')

	paginator = Paginator(events, 10) # Show 10 events per page
	page = request.GET.get("page")

	try:
		events = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		events = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		events = paginator.page(paginator.num_pages)
	context = {'events': events}
	return render(request, "news_events/events_index.html", context)



def events_detail(request, event_id):
	try:
		event = Events.objects.get(id=event_id)
	except Events.DoesNotExist:
		raise Http404("The event does not exist")
	context = {"event": event}
	return render(request, "news_events/events_detail.html", context)


def news_index(request):
	news = News.objects.order_by('-pub_date')

	paginator = Paginator(news, 10) # Show 10 news per page
	page = request.GET.get("page")

	try:
		news = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		news = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		news = paginator.page(paginator.num_pages)
	context = {'news': news}
	return render(request, "news_events/news_index.html", context)

def news_detail(request, news_id):
	try:
		news = News.objects.get(id=news_id)
	except News.DoesNotExist:
		raise Http404("The news does not exist")
	context = {"news": news}
	return render(request, "news_events/news_detail.html", context)