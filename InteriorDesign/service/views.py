from django.shortcuts import render
from .models import Service, TeamMember


def index(request):
	services = Service.objects.all()
	teammembers = TeamMember.objects.all()
	context = {
		'services': services,
		'teammembers': teammembers
	}
	return render(request, 'index.html', context)