import pandas as pd 
import os
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column, layout
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.palettes import Category10_10
from bokeh.models.widgets import Panel, Tabs
import itertools
from bokeh.models.widgets import PreText, Div
import datetime

################################################################### Bar graph ###############################################################################################
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

######################################## Line Graph with new death trends for the four most populous countries in the world for past week ####################################

last_week_dates = []
for i in range(0,7):
    date = datetime.date.today() - datetime.timedelta(days=i)
    last_week_dates.insert(0, str(date))
    
dates = last_week_dates # creates plots for the last seven
countries =['China','India','USA','Indonesia', 'Brazil']# five most populous countries

conditions = ['NewDeaths', 'TotalDeaths', 'TotalCases', 'Deaths/1M pop', 'Population', '1 Deathevery X ppl', 'New Deaths/1M pop']

#condition = 'NewDeaths' # condition should be able to change using Dropdown widget 
#condition1 = 'TotalDeaths'

def data_organizer(countries, dates, condition):
    data = {}
    for date in dates: # This double loop organizes the dat and creates the data frame used as the source in bokeh plotting
    
        #try block for if data is missing for a particular date
        try: 
            tempdf= pd.read_json(f'{os.getcwd()}/project_data_json/covidinfo{date}.json', orient ='index')
            tempdf.set_index('Country,Other')
            tempdf = tempdf.replace(',','', regex=True)
            countrydata = {}
            #countrydata1 = {}
            for country in countries: 
                countrydata[country] = tempdf.at[country,condition].replace('+','')
                #countrydata1[country] = tempdf.at[country,condition1].replace('+', '')
            data[date] = countrydata
            #data1[date] = countrydata1
        except:
            print('We did not save data for that date')
    return data

# These next few lines create and reorganize the dataframe 
final = pd.DataFrame(data_organizer(countries, dates, conditions[0]))
final1 = pd.DataFrame(data_organizer(countries, dates, conditions[1]))

final = final.T
final1 = final1.T

final['dates'] = final.index
final1['dates'] = final1.index

final = final.replace(r'^\s*$', 0, regex=True) # replaces blank values with zero 
final1 = final1.replace(r'^\s*$', 0, regex=True) 

output_file('Country_overTime.html')
color = iter(Category10_10)# allows for chaninging color each iteration of plotting loop 
color2 = iter(Category10_10)

countryGraph = figure(title = f'Seven Day {conditions[0]} Trend for 5 most populous countries (click items in legend to toggle visibility)',
                      x_axis_label = 'Dates',y_axis_label = conditions[0],
                      x_range = dates, plot_width = 1000, plot_height = 1000, 
                      tools = 'pan,box_select,zoom_in,zoom_out,')


countryGraph1 = figure(title = f'Seven Day {conditions[1]} Trend for 5 most populous countries (click items in legend to toggle visibility)',
                      x_axis_label = 'Dates',y_axis_label = conditions[1],
                      x_range = dates, plot_width = 1000, plot_height = 1000, 
                      tools = 'pan,box_select,zoom_in,zoom_out,')

source = ColumnDataSource(final)
source1 = ColumnDataSource(final1)

for (name, data )in final.iteritems(): # loops through and plots each countries trendline
    if(name != 'dates'):
        countryGraph.line('dates',name,source = source,legend_label = name,line_width = 1, color = next(color))

for (name, data )in final1.iteritems(): # loops through and plots each countries trendline
    if(name != 'dates'):
        countryGraph1.line('dates',name,source = source1,legend_label = name,line_width = 1, color = next(color))

intro = PreText(text ='Welcome to our Covid Dashboard!',width=500, height=100,
                style={'font-size':'40pt', 
                     'color': 'black', 
                     'font-weight': 'bold', 
                     'font-family': 'Arial, Helvetica, sans-serif'})

countryGraph.legend.location = 'top_right'
countryGraph.legend.click_policy = 'hide'

countryGraph1.legend.location = 'top_right'
countryGraph1.legend.click_policy = 'hide'

tab_new_deaths = Panel(child = countryGraph, title = 'New Deaths')
tab_total_deaths = Panel(child = countryGraph1, title = 'Total Deaths')

tabs = Tabs(tabs = [tab_new_deaths, tab_total_deaths])

p.add_tools(hover)

layout = layout(intro,p,tabs)

show(layout)