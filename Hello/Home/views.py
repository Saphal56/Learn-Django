from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse ("This is HomePage ")

def about(request):
    return HttpResponse ("This is AboutPage ")

def services(request):
    return HttpResponse ("This is ServicePage ")

def contact(request):
    return HttpResponse ("This is contactPage ")