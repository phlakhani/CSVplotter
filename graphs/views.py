import plotly
import plotly.graph_objs as go

from django.shortcuts import render
from csvdata.dataprocess import exportCSVdata
# Create your views here.

def home(request):

    return render(request, 'graphs_list.html')


def LineGraph(request):

    dataset = exportCSVdata()
    allcols = list(dataset.columns)
    totalrecords = dataset.shape[0]

    if request.method=='POST':
        x_data_string = request.POST['rangeNo'].strip()
        for i in x_data_string:
            if i==':':
                k = x_data_string.index(i)
                x_1strange = int(x_data_string[:k])
                x_2strange = int(x_data_string[k+1:])

        x_data = request.POST['x_axis'].strip()
        y_data = request.POST['y_axis'].strip()
        x_plot = dataset[x_1strange:x_2strange][x_data]
        y_plot = dataset[x_1strange:x_2strange][y_data]


        scatter = go.Scatter(x=x_plot, y=y_plot, mode='lines',  marker_color='green')

        layout = go.Layout(title=f"{x_data} vs. {y_data}", xaxis={'title':f'{x_data}'}, yaxis={'title':f'{y_data}'})

        fig = go.Figure(data = [scatter], layout=layout)
        #plt_div = plot(fig, output_type='div') # can be used to convert plot to html code as well
        plt_div =  fig.to_html(full_html=True)

        context = { 'totalrecords':totalrecords,
                    'allcols':allcols,
                    'plot_div':plt_div
                    }

        return render(request, 'line_graph.html', context)
    else:
        context = {'totalrecords':totalrecords,
                   'allcols':allcols
                   }
        return render(request, 'line_graph.html',context)


def BarGraph(request):

    dataset = exportCSVdata()
    allcols = list(dataset.columns)
    totalrecords = dataset.shape[0]

    if request.method == 'POST':
        x_data_string = request.POST['rangeNo'].strip()
        for i in x_data_string:
            if i == ':':
                k = x_data_string.index(i)
                x_1strange = int(x_data_string[:k])
                x_2strange = int(x_data_string[k + 1:])

        x_data = request.POST['x_axis'].strip()
        y_data1 = request.POST['y_axis1'].strip()
        y_data2 = request.POST['y_axis2'].strip()
        y_data3 = request.POST['y_axis3'].strip()
        x_plot = dataset[x_1strange:x_2strange][x_data]
        y_plot1 = dataset[x_1strange:x_2strange][y_data1]
        y_plot2 = dataset[x_1strange:x_2strange][y_data2]
        y_plot3 = dataset[x_1strange:x_2strange][y_data3]


        bar1 = go.Bar(name=f'{y_data1}', x=x_plot, y=y_plot1)
        bar2 = go.Bar(name=f'{y_data2}', x=x_plot, y=y_plot2)
        bar3 = go.Bar(name=f'{y_data3}', x=x_plot, y=y_plot3)

        layout = go.Layout(title=f"Bar graph for {x_data} over  {y_data1}, {y_data2} & {y_data3}" )

        fig = go.Figure(data= [bar1, bar2, bar3], layout= layout)
        plt_div = fig.to_html(full_html=True)

        context = { 'totalrecords': totalrecords,
                    'allcols': allcols,
                    'plot_div': plt_div
                    }

        return render(request, 'bar_graph.html', context)
    else:
        context = {'totalrecords': totalrecords,
                   'allcols': allcols
                   }
        return render(request, 'bar_graph.html', context)


def PieGraph(request):

    dataset = exportCSVdata()
    allcols = list(dataset.columns)
    totalrecords = dataset.shape[0]

    if request.method == 'POST':
        x_data_string = request.POST['rangeNo'].strip()
        for i in x_data_string:
            if i == ':':
                k = x_data_string.index(i)
                x_1strange = int(x_data_string[:k])
                x_2strange = int(x_data_string[k + 1:])

        category_data = request.POST['categories'].strip()
        values_data = request.POST['values'].strip()
        category_plot = dataset[x_1strange:x_2strange][category_data]
        values_data_plot = dataset[x_1strange:x_2strange][values_data]

        layout = go.Layout(title=f"Segmentwise percentages of {values_data}  for  {category_data}")

        pie = go.Pie(labels = category_plot, values = values_data_plot)
        fig = go.Figure(data= [pie], layout= layout)
        plt_div = fig.to_html(full_html=True)

        graphtitle = f'{category_data} vs. {values_data}'
        context = {'graphtitle': graphtitle, 'totalrecords': totalrecords, 'allcols': allcols, 'plot_div': plt_div}

        return render(request, 'pie_graph.html', context)
    else:
        context = {'totalrecords': totalrecords, 'allcols': allcols}

        return render(request, 'pie_graph.html', context)

def Histogram(request):

    dataset = exportCSVdata()
    allcols = list(dataset.columns)
    totalrecords = dataset.shape[0]

    if request.method == 'POST':
        x_data_string = request.POST['rangeNo'].strip()
        for i in x_data_string:
            if i == ':':
                k = x_data_string.index(i)
                x_1strange = int(x_data_string[:k])
                x_2strange = int(x_data_string[k + 1:])

        hist_array = request.POST['hist_array'].strip()
        bin_size = int(request.POST['bin_size'].strip())
        hist_array_plot = dataset[x_1strange:x_2strange][hist_array]

        layout = go.Layout(title=f" Value Distribution for {hist_array}")

        hist = go.Histogram(x = hist_array_plot, nbinsx=bin_size)
        fig = go.Figure(data=[hist], layout=layout)
        plt_div = fig.to_html(full_html=True)

        context = {'totalrecords': totalrecords,
                   'allcols': allcols,
                   'plot_div': plt_div
                   }
        return render(request, 'histogram.html', context)
    else:
        context = {'totalrecords': totalrecords,
                   'allcols': allcols
                   }
        return render(request, 'histogram.html', context)

def ScatterGraph(request):
    dataset = exportCSVdata()
    allcols = list(dataset.columns)
    totalrecords = dataset.shape[0]

    if request.method == 'POST':
        x_data_string = request.POST['rangeNo'].strip()
        for i in x_data_string:
            if i == ':':
                k = x_data_string.index(i)
                x_1strange = int(x_data_string[:k])
                x_2strange = int(x_data_string[k + 1:])

        x_data = request.POST['x_axis'].strip()
        y_data = request.POST['y_axis'].strip()
        x_plot = dataset[x_1strange:x_2strange][x_data]
        y_plot = dataset[x_1strange:x_2strange][y_data]

        scatter = go.Scatter(x=x_plot, y=y_plot, mode='markers', marker_color='green')

        layout = go.Layout(title=f"{x_data} vs. {y_data}", xaxis={'title': f'{x_data}'}, yaxis={'title': f'{y_data}'})

        fig = go.Figure(data=[scatter], layout=layout)
        # plt_div = plot(fig, output_type='div') # can be used to convert plot to html code as well
        plt_div = fig.to_html(full_html=True)

        context = {'totalrecords': totalrecords,
                   'allcols': allcols,
                   'plot_div': plt_div
                   }

        return render(request, 'scatter_graph.html', context)
    else:
        context = {'totalrecords': totalrecords,
                   'allcols': allcols
                   }
        return render(request, 'scatter_graph.html', context)

def BoxPlot(request):
    dataset = exportCSVdata()
    allcols = list(dataset.columns)
    totalrecords = dataset.shape[0]

    if request.method == 'POST':
        x_data_string = request.POST['rangeNo'].strip()
        for i in x_data_string:
            if i == ':':
                k = x_data_string.index(i)
                x_1strange = int(x_data_string[:k])
                x_2strange = int(x_data_string[k + 1:])

        plot_1_data = request.POST['plot_1'].strip()
        plot_2_data = request.POST['plot_2'].strip()
        plot_1 = dataset[x_1strange:x_2strange][plot_1_data]
        plot_2 = dataset[x_1strange:x_2strange][plot_2_data]

        plot1 = go.Box(y=plot_1 )
        plot2 = go.Box(y=plot_2)

        layout = go.Layout(title=f"Box plot for column {plot_1_data} and  {plot_2_data}" )

        fig = go.Figure(data=[plot1, plot2], layout=layout)
        # plt_div = plot(fig, output_type='div') # can be used to convert plot to html code as well
        plt_div = fig.to_html(full_html=True)

        context = {'totalrecords': totalrecords,
                   'allcols': allcols,
                   'plot_div': plt_div
                   }

        return render(request, 'box_plot.html', context)
    else:
        context = {'totalrecords': totalrecords,
                   'allcols': allcols
                   }
        return render(request, 'box_plot.html', context)


