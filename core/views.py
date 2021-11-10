from django.shortcuts import render
import pandas as pd
from plotly.offline import plot
import plotly.graph_objects as go
import plotly.express as px 

# py.init_notebook_mode(connected=False)

# Create your views here.

def barras(request):
    
    # Carregando os dados
    df = pd.read_csv('media/data.csv')

    # Criando gráfico
    trace = go.Scatter(x = df['yr_built'],
                    y = df['price'],
                    mode = 'markers')

    # Armazenando gráfico em uma lista
    data = [trace]

    # Criando Layout
    layout = go.Layout(title='Preços por ano de construção',
                    yaxis={'title':'Preço da casa'},
                    xaxis={'title': 'Ano de construção'})

    # Criando figura que será exibida
    fig = go.Figure(data=data, layout=layout)

    plot_div = plot({'data': data, 'layout': layout}, 
                    output_type='div')

    return render(request, "index.html", 
                  context={'fig': plot_div})

def mapa(request):

    # Carregando os dados
    df = pd.read_csv('static/cidades.csv')
    trace = go.Scattergeo(
                     locationmode = 'USA-states',
                     lon = df['lon'],
                     lat = df['lat'],
                     text = 'Nome da cidade: ' + df['name'], 
                     marker = dict(
                            color = '#e74c3c',
                            line = {'width': 0.5, 
                                    'color': '#2c3e50'},
                            sizemode = 'area')
    )

    data = [trace]

    layout = go.Layout(
        title = '<b>Mapa</b>',
        titlefont = {'family': 'Arial',
                     'size': 24},
        geo =  {'scope': 'usa',
                'projection': {'type': 'albers usa'},
                'showland': True,
                'landcolor': '#2ecc71',
                'showlakes': True,
                'lakecolor': '#3498db',
                'subunitwidth': 1,
                'subunitcolor': "rgb(255, 255, 255)"
                })

    fig = go.Figure(data=data, layout=layout)

    plot_div = plot({'data': data, 'layout': layout}, 
                    output_type='div')

    return render(request, "mapa.html", 
                  context={'fig': plot_div})

def pizza(request):
    
    # Carregando os dados
    df = pd.read_csv('static/cidades.csv')

    labels = [1,2,3,4]
    values = [10,20,30,40]
    
    plt = px.pie(labels, values=values, names=labels, title='Population of European continent')

    plot_div = plot(plt, output_type='div')
  
    return render(request, "mapa.html", 
                  context={'fig': plot_div})
