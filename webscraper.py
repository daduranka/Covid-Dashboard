# Practicing Data Scraping from worldometer, grabs main data table from website and saves it as a csv

#adding date time module to distinguish data from different days
from datetime import date
import json

from bs4 import BeautifulSoup
import requests
import pandas as pd # for dataframe creation
html_text = requests.get('https://www.worldometers.info/coronavirus/').text # inspects site
soup = BeautifulSoup(html_text, 'lxml') # lxml is apperently best 
table = soup.find('table',id = 'main_table_countries_today') # finds main table 
column_names= []
for column in table.find_all('th'): # gets all column names and puts them in a list for creation of data frame 
    name = column.text
    column_names.append(name)
column_names[13] = 'Tests/1M pop' # this name was wrapped and gave errors unless manually changed 
csvfile = pd.DataFrame(columns = column_names)
for row in table.find_all('tr')[1:]:
    data = row.find_all('td')
    data_text = [section.text for section in data]
    location = len(csvfile)
    csvfile.loc[location] = data_text

today = date.today()    #grabbing today's date    
csvfile.to_json(f'rawcovidinfo{today}.json', orient = 'index') #storing data in json format with today's date in title



data = json.loads(open(f'rawcovidinfo{today}.json').read()) #

for key in data:
        new_key = data[key]['Country,Other']
        death_rates[new_key] = data[key]


death_rates = {}    #creating empty dictionary for death_rates_data





#print(death_rates)
        
