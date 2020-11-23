from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def one_method(request):
    return HttpResponse("Yeah... It works")

def another_method(request, my_val):
    pass

def yet_another_method(request, name):
    pass

def one_more_method(request, id, color):
    pass