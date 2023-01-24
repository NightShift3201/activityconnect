from django.shortcuts import render
from django.http import HttpResponse
from .models import Activity, Day
from django.db.models import Q
from django.shortcuts import redirect


def index(request):
    return redirect('/home')

def aboutUs(request):
    return HttpResponse(request, 'main/about_us.html')

def home(request):
    activty_list = Activity.objects.all()
    context = {
        'activty_list' : activty_list
    }
    return render(request, 'main/home.html',context)

def view_activity(request, activity_name):
    activity_name = activity_name.replace('_', ' ')
    activity = Activity.objects.get(title=activity_name)
    category = request.GET.get('category')
    context = {
        'activity': activity,
        'category': category
    }
    return render(request, 'main/activity.html', context)

def view_category(request, category_name):

    if category_name=="all":
        activty_list = Activity.objects.all()
    else:
        activty_list = Activity.objects.filter(tags__name__in=[category_name])
    context = {
        'activty_list' : activty_list,
        'category' : category_name.capitalize()
    }
    return render(request, 'main/home.html',context)



def search(request):
    if request.method == 'GET':
        query = request.GET.get('query')

        if query:
            activty_list = Activity.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
            context = {
                'activty_list': activty_list
            }
        else:
            activty_list = Activity.objects.all()
            context = {
                'activty_list': activty_list
            }
        return render(request, 'main/home.html', context)
    else:
        activty_list = Activity.objects.all()
        context = {
            'activty_list': activty_list
        }
        return render(request, 'main/home.html', context)

