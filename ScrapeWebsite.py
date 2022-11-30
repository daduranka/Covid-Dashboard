# Module for scraping data and returning deaths in a country, 
#contains the function scrape_country which takes a country and the website to scrape data from 
# we use the website worldometer for data scraping 
from bs4 import BeautifulSoup
import requests
import pandas as pd # for dataframe creation

def scrape_country(country,url):
    html_text = requests.get(url).text
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
    
        
    