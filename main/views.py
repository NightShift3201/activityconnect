from django.shortcuts import render
from django.http import HttpResponse
from .models import Activity
from django.db.models import Q

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
    if category_name=="all":
        activty_list = Activity.objects.all()
    else:
        activty_list = Activity.objects.filter(tags__name__in=[category_name])
    context = {
        'activty_list' : activty_list
    }
    return render(request, 'main/home.html',context)



def search(request):
  if request.method == 'POST':
    query = request.POST.get('query')

    activty_list = Activity.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    context = {
        'activty_list' : activty_list
    }

    return render(request, 'main/home.html', {'activty_list': activty_list})
  else:
    activty_list = Activity.objects.all()
    context = {
        'activty_list' : activty_list
    }
    return render(request, 'main/home.html',context)

