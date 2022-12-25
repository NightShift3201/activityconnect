from django.shortcuts import render
from django.http import HttpResponse
from .models import Activity

def index(request):
    return HttpResponse("Activity Connect!")

def home(request):
    activty_list = Activity.objects.all()
    context = {
        'activty_list' : activty_list
    }
    return render(request, 'main/home.html',context)