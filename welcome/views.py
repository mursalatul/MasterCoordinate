from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def welcome_page(request):
    # importing welcome_page_template1.html
    w_p_t1 = loader.get_template("welcome_page_template1.html")
    return HttpResponse(w_p_t1.render())

def show_options(request):
    x1 = request.GET['x1']
    y1 = request.GET['y1']

    # if data attached
    if x1 and y1:
        show_page = loader.get_template("show_coordinates_template1.html")
        context = {
            "p" : [x1, y1],
        }
        return HttpResponse(show_page.render(context, request))
    else:
        # if one of the datas is missing
        return HttpResponse("empty input")
