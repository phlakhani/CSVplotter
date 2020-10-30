from django.urls import path
from .views import home, LineGraph, BarGraph, PieGraph, Histogram, ScatterGraph, BoxPlot



urlpatterns = [
    path('graphs/', home, name='graphs_list'),
    path('line_graph/', LineGraph, name='line_graph'),
    path('bar_graph/', BarGraph, name='bar_graph'),
    path('pie_graph/', PieGraph, name='pie_graph'),
    path('histogram/', Histogram, name='histogram'),
    path('scatter_graph/', ScatterGraph, name='scatter_graph'),
    path('box_plot/', BoxPlot, name='box_plot'),
   ]