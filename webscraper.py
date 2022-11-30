# Practicing Data Scraping from worldometer, grabs main data table from website and saves it as a csv


from bs4 import BeautifulSoup
import requests
import pandas as pd # for dataframe creation
html_text = requests.get('https://www.worldometers.info/coronavirus/').text
soup = BeautifulSoup(html_text, 'lxml')
table = soup.find('table',id = 'main_table_countries_today')
column_names= []
for column in table.find_all('th'):
    name = column.text
    column_names.append(name)
column_names[13] = 'Tests/1M pop'
csvfile = pd.DataFrame(columns = column_names)
for row in table.find_all('tr')[1:]:
    data = row.find_all('td')
    data_text = [section.text for section in data]
    location = len(csvfile)
    csvfile.loc[location] = data_text
    
csvfile.to_csv('covidinfo.csv',index=False)