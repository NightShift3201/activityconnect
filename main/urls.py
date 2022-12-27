from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path("home/", views.home),
    path('activity/<str:activity_name>/', views.view_activity)
]