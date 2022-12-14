import bokeh
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap
from bokeh.models import Range1d
import os
import pandas as pd

df = pd.read_csv(f'{os.getcwd()}/project_data_csv/covidinfo.csv')
df = df.replace(',','', regex=True)

newdf = df[8:238]

output_file("index.html")

total_cases = df['TotalCases'].astype(int)
total_cases = total_cases.div(1000)
source = ColumnDataSource(dict(newdf))
countries = source.data['Country,Other'].tolist()


p = figure(y_range = countries, plot_width = 1000, plot_height = 1000, tools = "pan,box_select,zoom_in,zoom_out",)

p.hbar(y= 'Country,Other', right ='TotalDeaths', source = source, left = 0, height = 0.1)
p.wedge()

show(p)
