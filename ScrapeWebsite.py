# Module for scraping data and returning deaths in a country, 
#contains the function scrape_country which takes a country and the website to scrape data from 
# we use the website worldometer for data scraping 
from datetime import date   #adding date
from bs4 import BeautifulSoup
import requests
import pandas as pd # for dataframe creation
import json         #for josn database storage


#Should we make the url value be an optional arugment and have the default be url = 'https://www.worldometers.info/coronavirus/'? That way it will usually be worldometer 
def scrape_country(country,url = 'https://www.worldometers.info/coronavirus/', date = date.today()):
    #make this an if statement so we only do this if we don't have the data for the specific date yet. 
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
    
    countries_dict = {}    #creating empty dictionary for death_rates_data
    for i in range(len(csvfile)):                                           #making covid data searchable by country in a new dictionary
        new_key = csvfile['Country,Other'][i]
        countries_dict[new_key] = {'TotalDeaths': csvfile['TotalDeaths'][i], 'NewDeaths': csvfile['NewDeaths'][i], 'Deaths/1M pop': csvfile['Deaths/1M pop'][i], 'New Deaths/1M pop': csvfile['New Deaths/1M pop'][i]}
    
    if date > date.today():
        return "Sorry we don't have data on that day yet."
    else: 
        if date == date.today():   #if today's date is selected create json file with raw data for today
            with open(f'rawcovidinfo{date}.json', 'w', encoding='utf-8') as jsonfile:
                jsonfile.write(json.dumps(countries_dict, indent=4)) #storing data in json format with today's date in title
        
    data = json.loads(open(f'rawcovidinfo{date}.json').read()) #grab past data or current data for country ####add try and except here

    death_rates = {} # creating empty dictionary to return data

    if country in countries_dict:                                 #searching dictionary for country and returning raw and normalized data
        if data[country]['TotalDeaths'] != '':
            
            death_rates[f'{country} Raw Cumulative Deaths'] = data[country]['TotalDeaths'].strip()
        
        else:
            death_rates[f'{country} Raw Cumulative Deaths'] = 'N/A'    
        
        
        if data[country]['NewDeaths'] != '':
        
            death_rates[f'{country} Raw Daily Deaths'] = data[country]['NewDeaths'].strip('+')
        
        else:
        
            death_rates[f'{country} Raw Daily Deaths']= 'N/A'  
        
        
        if data[country]['Deaths/1M pop'] != '':
        
            death_rates[f'{country} Normalized Cumulative Deaths(/1M)'] = data[country]['Deaths/1M pop']
        
        else:
        
            death_rates[f'{country} Normalized Cumulative Deaths(/1M)']= 'N/A'              

        
        if data[country]['New Deaths/1M pop'] != '':
        
            death_rates[f'{country} Normalized Daily Deaths(/1M)'] = data[country]['New Deaths/1M pop']
        
        else:
        
            death_rates[f'{country} Normalized Daily Deaths(/1M)']= 'N/A'                  
            
    else:
        print("Sorry we don't have data for that country/region at the moment")
        
    return death_rates    

    
#used to test functionality
#countries with expected return values
print(f"America data for today: {scrape_country('USA')}")
print(f"Germany data for today: {scrape_country('Germany')}")
print(f"Cook Islands data for today: {scrape_country('Cook Islands')}")


#testing incorrect country name
print(f"America data for today(incorrect country name): {scrape_country('America')}")

#testing incorrect date
print(f"America data for today: {scrape_country('USA', 'https://www.worldometers.info/co','2022-12-25')}")