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

################################################### Needs Modification #############################################################################################################
#(function is based off of geeksforgeeks tutorial)
#Description: This function takes in a path to a file and destinaation and reads the data from the file, converts it into JSON format and stores the data. Its purpose is to
#             make file manipulation and searches for the covid dashboard possible.
#
#Inputs: filepath - path to csv file
#        destination - path to location for saving JSON file with data
#
#Returns: states_dict - nested dictionary containing the covid data
def json_file_writer(filepath, destination):
    
    #dictionary for holding state by state data
    states_dict = {}
              
    # create a csv reader
    with open(filepath, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        # Convert each row into a dictionary
        # and add it to data
        for rows in reader:        
            #assigning the state column to be the key simulating different country names #####ONLY SAVING WYOMING, NEED DIFFERENT METHOD FOR DETERMINING KEYS
            key = rows['\ufeffdate'] 
            states_dict[key] = rows       
        
        for dict_key in states_dict:
            states_dict[dict_key]['date'] =  states_dict[dict_key].pop('\ufeffdate')  
     
    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(destination, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(json.dumps(states_dict, indent=4))
    
    return states_dict
##############################################################################################################################################################################         


######################################################### Needs to be modified ###############################################################################################
#Function: raw_data 
#Description: This function computes the raw cumulative death rates and raw daily death rates for a specific state (eventually country). Cumulative death rates sum the deaths 
#             everyday up to and including the specified date. Daily death rates list the number of deaths that occurred on that specific date. 
#
#Inputs: state - name of the state user wants data from
#        date - month, day, and year that user wants data from
#
#Returns: death_rates - dictionary of the daily and cumulative death rates in a specific state for a specific date
def raw_data(state, date):
    
    file_path = os.getcwd() + "/states covid deaths.csv"
    store_path = 'stored_data_temp.json'
    
    covid_data = {}
    
    raw_cumulative = 0
    raw_daily = 0
    
    covid_data = json_file_writer(file_path, store_path)
    
    print(covid_data[date])
    

data_dict = {}

current_path = os.getcwd()

file_Path = f'{current_path}/states covid deaths.csv'
database_path = 'stored_data.json'
 
# Call the make_json function
data_dict = json_file_writer(file_Path, database_path)

raw_data('Alabama', '11/27/2022')

