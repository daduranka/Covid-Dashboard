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

#function is based off of geeksforgeeks tutorial
def json_file_writer(filepath, destination):
    
    #dictionary for holding state by state data
    states_dict = {}
              
    # create a csv reader
    with open(filepath, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        # Convert each row into a dictionary
        # and add it to data
        for rows in reader:        
            #assigning the state column to be the key simulating different country names
            key = rows['\ufeffdate'] 
            states_dict[key] = rows       
            print(states_dict)
            #key = rows['date']
            
            #key = rows['\ufeffdate']
            #states_dict[key] = rows

    
    # Open a json writer, and use the json.dumps()
    # function to dump data
    #with open(destination, 'w', encoding='utf-8') as jsonfile:
    #    jsonfile.write(json.dumps(states_dict, indent=4))
         

current_path = os.getcwd()

file_Path = f'{current_path}/states covid deaths.csv'
database_path = 'stored_data.json'
 
# Call the make_json function
json_file_writer(file_Path, database_path)