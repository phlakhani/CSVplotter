from plotly.offline import plot
import plotly.graph_objs as go

from django.shortcuts import render
from csvdata.dataprocess import exportCSVdata
# Create your views here.
def home(request):

    return render(request, 'graphs_list.html')


def LineGraph(request):

    dataset = exportCSVdata()
    if request.method=='POST':
        x_data_string = request.POST['rangeNo']
        for i in x_data_string:
            if i==':':
                k = x_data_string.index(i)
                x_1strange = int(x_data_string[:k])
                x_2strange = int(x_data_string[k+1:])


        y_data = request.POST['column']
        x_plot = dataset[x_1strange:x_2strange]['#']
        y_plot = dataset[x_1strange:x_2strange][y_data]

    fig = go.Figure()
    scatter = go.Scatter(x=[1,2,3,5,6], y=[12,10,8,6,17],
                         mode='lines', name='test',
                         opacity=0.8, marker_color='green')
    fig.add_trace(scatter)
    plt_div = plot(fig, output_type='div')

    context = {'plot_div':plt_div}
    return render(request, 'line_graph.html', context)