from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request, 'tagalong/index.html')

def get_animals(request):
	pass
	
