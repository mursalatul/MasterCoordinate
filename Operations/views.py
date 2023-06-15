from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def distance(request, x1, y1):
    # calculating distance between point x1, y1
    return HttpResponse("calculating Distance")

def dotproduct(request, x1, y1):
    return HttpResponse("calculating dot product")

def crossproduct(request, x1, y1):
    return HttpResponse("calculating cross product")

