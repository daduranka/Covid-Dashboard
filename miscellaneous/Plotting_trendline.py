import pandas as pd 
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
import os
from bokeh.palettes import Category10_10
import itertools

dates = ['2022-11-30','2022-12-01','2022-12-03','2022-12-08','2022-12-09'] # test sample of dates should change using DateRangeSlider 
countries =['USA','China','Israel','Mexico','UK']# sample selection of countries, shuld be able to select countries using MultiChoice Widget
condition = 'NewDeaths' # condition should be able to change using Dropdown widget 
data ={}

for date in dates: # This double loop organizes the dat and creates the data frame used as the source in bokeh plotting
    tempdf= pd.read_json(f'{os.getcwd()}/project_data_json/covidinfo{date}.json', orient ='index')
    tempdf.set_index('Country,Other')
    tempdf = tempdf.replace(',','', regex=True)
    countrydata = {}
    for country in countries: 
        countrydata[country] = tempdf.at[country,condition].replace('+','')
    data[date] = countrydata
    
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

                

show(countryGraph)
