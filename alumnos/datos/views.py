from django.shortcuts import render
from django.http import HttpResponse


def hola(request):
	return HttpResponse("Hellos world desde django")
# Create your views here.
