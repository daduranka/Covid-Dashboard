# Covid-Dashboard

Class: ME EN 6250
Students: Eli Finlinson, Braden Brown

This repository contains the code for the ME EN 6250 Covid Dashboard assignment. The goal of this code is to allow users to compare Covid data between different countries. This goal is accomplished by creating a website of interactive plots using Python modules such as the Bokeh library. 

SET-UP: 

For the each of the files to run properly, the following modules need to be installed on your computer:

    Pandas - install using command 'pip install pandas'

    Beautiful Soup - install using command 'pip install beautifulsoup4'

    Requests - install using command 'pip install requests'

    Bokeh - install using command 'pip install Bokeh'

All other modules used are built into the Python standard library and should be avaible with up to date verisons of Python. 

INTENDED USE and ASSUMPTIONS:

The code written is intended for use to display a simple covid dashboard that displays data on covid for countries around the world. All data is scraped from the website "https://www.worldometers.info/coronavirus/" and is assumed to be accurate. 

FEATURES and INSTRUCTIONS:
    
The main scirpt that needs to be ran is the "Both_Graphs.py" script. This will open and save an HTML file containing a bar graph displaying the total deaths for each country from Covid. The data can be better explored and seen by using the Bokeh embeded zoom tool and the hover tool, which allows the user to hover the cursor over a bar in the graph and see more data on the country of interest. The second graph shows recent trends for new covid cases, for the four most populous countries in the world (China, India, Indonesia, and the USA). To run the "Both_Graphs.py" script you need to have the "project_data_json" file in the same directory. 
