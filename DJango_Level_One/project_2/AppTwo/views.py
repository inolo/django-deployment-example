from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "apptwo/index.html",{
        "insert_me": "Hello I am from views.py"
    })