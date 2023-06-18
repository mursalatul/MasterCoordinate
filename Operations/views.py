from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

from math import sqrt, pow

def distance(request, x1, y1, x2, y2):
    # calculating distance between point x1, y1
    dis = sqrt((pow(int(x1) - int(x2), 2)) + (pow(int(y1) - int(y2), 2)))

    # loading html file
    dis_html = loader.get_template("distance.html")
    context = {
        'p' : [x1, y1, x2, y2],
        'calculated_distance' : dis
    }
    return HttpResponse(dis_html.render(context))

def dotproduct(request, x1, y1, x2, y2):
    # calculating dot product between point x1, y1
    dpro = int(x1) * int(x2) + int(y1) * int(y2)

    # loading html file
    dpro_html = loader.get_template("dotproduct.html")
    context = {
        'p' : [x1, y1, x2, y2],
        'calculated_dotproduct' : dpro
    }
    return HttpResponse(dpro_html.render(context))

def crossproduct(request, x1, y1, x2, y2):
    # calculating cross product between point x1, y1
    cpro = int(x1) * int(y2) - int(x2) * int(y1)

    # loading html file
    cpro_html = loader.get_template("crossproduct.html")
    context = {
        'p' : [x1, y1, x2, y2],
        'calculated_crossproduct' : cpro
    }
    return HttpResponse(cpro_html.render(context))
