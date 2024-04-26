# Step3 of Final project : global_covid_data_analysis.py file has a logic to analyse COVID data retrieved and 
# aggregates the confimed and death cases for all countries across the globe
# Author: Simranbir Kaur
# Student Id: 000490704

import covid_data_loader
import pandas as pd

# method for transforming the confirmed covid cases data
def analyseCovidConfirmedCases():
   #Getting the confirmed covid cases by calling a function inside dataLoader class
   df_confirmed_cases = covid_data_loader.fetch_covid_confirmed_cases()
   
   #Creating a copy of df_confirmed_cases for modifications
   df_cc = df_confirmed_cases.copy()
   
   #Dropping the columns 'Country/Region', 'Province/State', 'Lat', 'Long'
   df_cc = df_cc.drop(['Country/Region', 'Province/State', 'Lat', 'Long'], axis=1)
   
   #Inverting the data inside the dataframe
   df_cc = df_cc.transpose()
   
   #Summing confirmed cases for all the countries (daily total of all the countries)
   df_cc = df_cc.sum(axis=1)

   #Adding headers 
   # Convert the Series to a DataFrame with one column
   dfcc_with_headers = pd.DataFrame(df_cc, columns=['Value'])

   # Reset the index to add the 'Date' column
   dfcc_with_headers.reset_index(inplace=True)
   dfcc_with_headers.columns = ['Date', 'Confirmed_Cases']

   # Changing the date format of Date Column
   dfcc_with_headers['Date'] = pd.to_datetime(dfcc_with_headers['Date']).dt.strftime('%Y-%m-%d')

   return dfcc_with_headers

# method for transforming the covid death cases data
def analyseCovidDeathCases():
   #Getting the death covid cases by calling a function inside dataLoader class
   df_death_cases = covid_data_loader.fetch_covid_death_cases()
   
   #Creating a copy of df_death_cases for modifications
   df_dc = df_death_cases.copy()
   
   #Dropping the columns 'Country/Region', 'Province/State', 'Lat', 'Long'
   df_dc = df_dc.drop(['Country/Region', 'Province/State', 'Lat', 'Long'], axis=1)
   
   #Inverting the data inside the dataframe
   df_dc = df_dc.transpose()
   
   #Summing confirmed cases for all the countries (daily total of all the countries)
   df_dc = df_dc.sum(axis=1)

   #Adding headers 
   # Convert the Series to a DataFrame with one column
   dfdc_with_headers = pd.DataFrame(df_dc, columns=['Value'])

   # Reset the index to add the 'Date' column
   dfdc_with_headers.reset_index(inplace=True)
   dfdc_with_headers.columns = ['Date', 'Death_Cases']

   # Changing the date format of Date Column
   dfdc_with_headers['Date'] = pd.to_datetime(dfdc_with_headers['Date']).dt.strftime('%Y-%m-%d')

   return dfdc_with_headers

# Method to aggregate the confirmed and death cases data frame required in Step 3
def aggregateCovidData():

   #Calling the above functions to get the data for both confirmed and death cases
   df_cc = analyseCovidConfirmedCases()
   df_dc = analyseCovidDeathCases()
 
   #Aggregating both the dataframes into one
   aggregated_df = pd.merge(df_cc, df_dc, on='Date', how='outer')

   #Saving the data to aggregated_covid_data.csv file
   aggregated_df.to_csv('data_csv/covid/aggregated_covid_data.csv', index=True)

   return aggregated_df

