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

def view_activity(request, activity_name):
    activity_name = activity_name.replace('_', ' ')
    activity = Activity.objects.get(title=activity_name)
    context = {'activity': activity}
    return render(request, 'main/activity.html', context)

def view_category(request, category_name):
    activty_list = Activity.objects.all()
    context = {
        'activty_list' : activty_list
    }
    return render(request, 'main/home.html',context)
