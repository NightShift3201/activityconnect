from django.shortcuts import render
from django.http import HttpResponse
from .models import Activity, Day
from django.db.models import Q
from django.shortcuts import redirect
from decimal import Decimal


def index(request):
    return redirect('/home')

def aboutUs(request):
    return render(request, 'main/about_us.html')

def hostEvent(request):
    return render(request, 'main/hostEvent.html')

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

    difficulty = request.GET.getlist('difficulty')
    if difficulty:
        activty_list = activty_list.filter(difficulty__in=difficulty)

    day = request.GET.getlist('day')
    if day:
        day_instances = Day.objects.filter(name__in=day)
        activty_list = activty_list.filter(Q(days_of_week__in=day_instances) | Q(days_of_week__name__icontains="everyday")).distinct()

    if 'min_price' in request.GET and 'max_price' in request.GET:
        min_price = Decimal(request.GET['min_price'])
        max_price = Decimal(request.GET['max_price'])
        activty_list = activty_list.filter(price__gte=min_price, price__lte=max_price)
    
    if 'min_age' in request.GET and 'max_age' in request.GET:
        min_age = Decimal(request.GET['min_age'])
        max_age = Decimal(request.GET['max_age'])
        activty_list = activty_list.filter(minAge__gte=min_age, minAge__lte=max_age)
        activty_list = activty_list.filter(minAge__gte=min_age, minAge__lte=max_age).distinct()

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

