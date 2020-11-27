from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    context ={
        "name" : "noelle",
        "favorite_color" : "turquoise",
        "pets" : ["Bruce", "Fitz", "Georgie"]
    }
    return render (request, "index.html", context)