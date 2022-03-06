from django.shortcuts import render
from first_app.models import AccessRecord, Topic, Webpage

# Create your views here.


def index(request):
    webpage = AccessRecord.objects.order_by('date')
    return render(request, "first_app/index.html",{
        "access": webpage
    })