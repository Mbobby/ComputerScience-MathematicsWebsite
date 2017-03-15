from django.shortcuts import render
from models import Faculty
# Create your views here.

def index(request):
	faculties = Faculty.objects.all()
	context = {'faculties': faculties}
	return render(request, "faculty/index.html", context)

def detail(request, faculty_id):
	try:
		faculty = Faculty.objects.get(id=faculty_id)
	except Faculty.DoesNotExist:
		raise Http404("The faculty does not exist")
	context = {"faculty": faculty}
	return render(request, "faculty/detail.html", context)
	