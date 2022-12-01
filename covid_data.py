##############################################################################################################################################################################
# Assignment: Covid Dashboard (Project Milestone 1)
#
# Students: Eli Finlinson, Braden Brown
#
# File description:
#   This file will store the data that has been scrapped from different websites and will compmute the raw daily death rates, raw cumulative death rates, normalized daily 
#   death rates, and normalized cumulative death rates. The normalized death rate values will be normalized to number of deaths/1,000,000. The normalized death rates will 
#   help show comparisons in death rates between countries even if they differ in population size. The data will be stored in JSON format and will be searchable by country 
#   name. 
#
# Methods:
#   This file will make use of the json module and will use the dump(), dumps(), load(), and loads() methods to manipulate, format, and save the data. 
##############################################################################################################################################################################
#including csv library for practice
import csv

#including json library for formatting options
import json

#including os library for file paths
import os

#including date from datetime library store data across days
from datetime import date

################################################### Needs Modification #############################################################################################################
#(function is based off of geeksforgeeks tutorial)
#Description: This function takes in a path to a file and destinaation and reads the data from the file, converts it into JSON format and stores the data. Its purpose is to
#             make file manipulation and searches for the covid dashboard possible.
#
#Inputs: filepath - path to csv file
#        destination - path to location for saving JSON file with data
#
#Returns: states_dict - nested dictionary containing the covid data ####Can potentially pair this funciton with webscraper.py for collecting data each day
def json_file_writer(filepath):
    
    today = date.today()  
    
    #dictionary for holding state by state data
    countries_dict = {}
              
    # create a csv reader
    with open(filepath, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        # Convert each row into a dictionary
        # and add it to data
        count = 0
        for rows in reader:        
            #assigning the country column to be the key in the countries_dict
            key = rows['Country,Other'] 
            countries_dict[key] = rows       
    
    #cleaning up data we don't need/want   #####Will optimize later 
    for country in countries_dict:
        countries_dict[country].pop('#')
        countries_dict[country].pop('NewCases') 
        countries_dict[country].pop('TotalRecovered') 
        countries_dict[country].pop('NewRecovered') 
        countries_dict[country].pop('ActiveCases')
        countries_dict[country].pop('Serious,Critical') 
        countries_dict[country].pop('TotalTests') 
        countries_dict[country].pop('Tests/1M pop') 
        countries_dict[country].pop('Continent')
        countries_dict[country].pop('1 Caseevery X ppl') 
        countries_dict[country].pop('1 Testevery X ppl') 
        countries_dict[country].pop('New Cases/1M pop') 
        countries_dict[country].pop('Active Cases/1M pop')
        countries_dict[country].pop('Tot\xa0Cases/1M pop') 
    
     
    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(f'covidinfo{today}.json', 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(json.dumps(countries_dict, indent=4))
    
    #return states_dict
##############################################################################################################################################################################         


######################################################### Needs to be modified ###############################################################################################
#Function: get_data 
#Description: This function computes the raw and normalzied cumulative death rates and the raw and cumulative daily death rates for a specific country. Cumulative death rates 
#             refer to all the deaths that have occurred since Jan 1, 2020. Daily death rates list the number of deaths that occurred on the specific date given; default being
#             today 
#
#Inputs: state - name of the state user wants data from
#        (optional) date - month, day, and year that user wants data from; default value is today's date
#
#Returns: death_rates - dictionary of the raw daily and raw cumulative death rates 
def get_data(country, date = date.today()):
    
    file_path = f"{os.getcwd()}/covidinfo{date}.json"
    
    death_rates = {} 
    
    data = json.loads(open(file_path).read())
    
    if country in data:
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

today = date.today()

current_path = os.getcwd()

file_Path = f'{current_path}/covidinfo{today}.csv'
#database_path = 'stored_data.json'
 
#Call the make_json function
json_file_writer(file_Path)


print(f"US Data: {get_data('USA')}")
print(f"Germany Data: {get_data('Germany')}")
print(f"Cook Islands Data: {get_data('Cook Islands')}")


