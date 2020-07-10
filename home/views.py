from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("your search from project urls came to app urls and the got to views")