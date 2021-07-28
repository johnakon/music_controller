from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def welcome(request):
    return HttpResponse("<h2>hello there</h2>")