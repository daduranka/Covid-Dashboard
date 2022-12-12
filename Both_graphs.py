import pandas as pd 
import os
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column, layout
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.palettes import Category10_10
import itertools
from bokeh.models.widgets import PreText, Div
import datetime

## Bar graph
df = pd.read_json(f'{os.getcwd()}/project_data_json/covidinfo2022-12-10.json',orient ='index')
df = df.replace(',','', regex=True)
newdf = df[8:238]
output_file("index.html")
source = ColumnDataSource(dict(newdf))

countries = source.data['Country,Other'].tolist()

p = figure(title = 'Total Deaths from Covid per country, use zoom, pan and hover tools to better explore the data',
           x_axis_label = 'Number of Deaths', y_axis_label = 'Country', y_range = countries, plot_width = 1000, 
           plot_height = 1000, tools = 'pan,box_select,zoom_in,zoom_out,reset')

p.hbar(y= 'Country,Other', right ='TotalDeaths', source = source, left = 0, height = 0.1)
p.wedge()

hover = HoverTool()
hover.tooltips=[
    ('Country', '@{Country,Other}'),
    ('Population', '@Population'),
    ('Total Cases', '@TotalCases'),
    ('Total Deaths', '@TotalDeaths')
]
last_week_dates = []
## Line Graph with new death trends for the four most populous countries in the world for past week
for i in range(0,7):
    date = datetime.date.today() - datetime.timedelta(days=i)
    last_week_dates.insert(0, str(date))
    
dates = last_week_dates # test sample of dates should change using DateRangeSlider 
countries =['China','India','USA','Indonesia']# four most populous countries
condition = 'NewDeaths' # condition should be able to change using Dropdown widget 
data ={}

for date in dates: # This double loop organizes the dat and creates the data frame used as the source in bokeh plotting
    try:
        tempdf= pd.read_json(f'{os.getcwd()}/project_data_json/covidinfo{date}.json', orient ='index')
        tempdf.set_index('Country,Other')
        tempdf = tempdf.replace(',','', regex=True)
        countrydata = {}
        for country in countries: 
            countrydata[country] = tempdf.at[country,condition].replace('+','')
        data[date] = countrydata
    except:
        print('We did not save data for that date')
# These next few lines create and reorganize the dataframe 
final = pd.DataFrame(data)
final = final.T
final['dates'] = final.index

final = final.replace(r'^\s*$', 0, regex=True) # replaces blank values with zero 

output_file('Country_overTime.html')
color = iter(Category10_10)# allows for chaninging color each iteration of plotting loop 

countryGraph = figure(title = f'Trend for selected countries for the selected data set: "{condition}"',
                      x_axis_label = 'Dates',y_axis_label = condition,
                      x_range = dates, plot_width = 1000, plot_height = 1000, 
                      tools = 'pan,box_select,zoom_in,zoom_out,')

source = ColumnDataSource(final)

for (name, data )in final.iteritems(): # loops through and plots each countries trendline
    if(name != 'dates'):
        countryGraph.line('dates',name,source = source,legend_label = name,line_width = 2, color = next(color))

intro = PreText(text ='Welcome to our Covid Dashboard!',width=500, height=100,
                style={'font-size':'40pt', 
                     'color': 'black', 
                     'font-weight': 'bold', 
                     'font-family': 'Arial, Helvetica, sans-serif'})

p.add_tools(hover)
layout = layout(intro,p,countryGraph)

show(layout)
