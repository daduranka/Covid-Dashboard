import pandas as pd 
import os
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool


df = pd.read_json('covidinfo2022-11-30.json',orient ='index')
df = df.replace(',','', regex=True)
newdf = df[8:238] # Only grabs countries index
output_file("index.html")
source = ColumnDataSource(dict(newdf))

countries = source.data['Country,Other'].tolist()


p = figure(title = 'Total Deaths from Covid per country, use zoom, pan and hover tools to better explore the data',
           x_axis_label = 'Number of Deaths', y_axis_label = 'Country', y_range = countries, plot_width = 1000, 
           plot_height = 1000, tools = 'pan,box_select,zoom_in,zoom_out,reset')


p.hbar(y= 'Country,Other', right ='TotalDeaths', source = source, left = 0, height = 0.1)
p.wedge()

hover = HoverTool() # allows for visualization of data by moving cursor over value  
hover.tooltips=[
    ('Country', '@{Country,Other}'),
    ('Population', '@Population'),
    ('Total Cases', '@TotalCases'),
    ('Total Deaths', '@TotalDeaths')
]

p.add_tools(hover)

show(p)
