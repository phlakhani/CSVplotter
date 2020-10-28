from django.urls import path
from .views import home, LineGraph


urlpatterns = [
    path('graphs/', home, name='graphs_list'),
    path('line_graph/', LineGraph, name='line_graph'),
   ]