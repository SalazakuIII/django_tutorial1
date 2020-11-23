from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

# Create your views here.
def root_method(request):
    return HttpResponse("String response from root_method")

def another_method(request):
    return redirect("/redirect_route")

def redirected_method(request):
    return JsonResponse({"response":"JSON response from the redirected method", "status": True})