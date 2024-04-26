# Step 4 of Final Project: For any given date, you should be able to create/generate a dataframe of the total confirmed cases 
# and deaths for all the countries in the world 
# (Hint: a dictionary where the date is the key, and the corresponding value is a dataframe).
# Author: Sagar Umeshkumar Patel (Student ID: 000491515)

import pandas as pd
import covid_data_analysis

def generate_datewise_dataframe():

# Fetching data from global_covid_data_analysis class and using aggregateCovidData which gives aggregated covid data
    result = covid_data_analysis.aggregateCovidData()
    date_columns = result.columns[2:]
 
# Create an empty dictionary to store DataFrames for each date
    dataframes_by_date = {}

    # Extract relevant columns for the current date
    for date in result['Date']:
        date_data = result[result['Date'] == date]

    # Store the result in the dictionary
        dataframes_by_date[date] = date_data
     
    return dataframes_by_date