import bokeh
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.palettes import Spectral5
from bokeh.transform import factor_cmap
from bokeh.models import Range1d
import os
import pandas as pd
from datetime import date
import numpy as np

df = pd.read_json(f'{os.getcwd()}/project_data_json/covidinfo{date.today()}.json')
df.head()
df = df.replace('','0', regex=True).replace(' ','0', regex=True)
total_cases = []
total_deaths = []
new_deaths = []
deaths_1M_pop = []
population = []
death_every_x_ppl = []
new_deaths_1M_ppl = []
countries = []
skip_count = 0
for country in df:
    if skip_count > 7:
        total_cases.append(int(df[country]['TotalCases'].replace(',', '')))
        total_cases_new = total_cases[:-1]
        total_deaths.append(int(df[country]['TotalDeaths'].replace(',','')))
        total_deaths_new = total_deaths[:-1]
        new_deaths.append(int(float(df[country]['NewDeaths'].replace(',', ''))))
        new_deaths_new = new_deaths[:-1]
        deaths_1M_pop.append(int(float(df[country]['Deaths/1M pop'].replace(',', ''))))
        deaths_1M_pop_new = deaths_1M_pop[:-1]
        population.append(int(df[country]['Population'].replace(',', '')))
        population_new = population[:-1]
        death_every_x_ppl.append(int(df[country]['1 Deathevery X ppl'].replace(',', '')))
        death_every_x_ppl_new = death_every_x_ppl[:-1]
        new_deaths_1M_ppl.append(int(float(df[country]['New Deaths/1M pop'].replace(',', ''))))
        new_deaths_1M_ppl_new = new_deaths_1M_ppl[:-1]
        countries.append(df[country]['Country,Other'].replace('0',' ').replace(',',''))
        countries_new = countries[:-1]
    else:
        skip_count += 1

output_file("index.html")

p = figure(y_range = countries_new, plot_width = 1000, plot_height = 1000, tools = "pan,box_select,zoom_in,zoom_out")

p.hbar(y= countries_new, right = total_cases_new, left = 0, height = 0.1)

p.wedge()

show(p)