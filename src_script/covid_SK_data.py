# Step 5 of Final Project: Extract the total confirmed cases and deaths for Saskatchewan into a dataframe. 
# Author: Sagar Umeshkumar Patel
# (Student ID: 000491515)

import pandas as pd
import covid_data_loader

#Transforming the Saskatchewan confirmed cases
def SaskatchewanCovidConfirmedCasesData():
    
#Calling fetch_covid_confirmed_cases in datLoader to get Global covid confirmed Cases
    df_confirmed_cases = covid_data_loader.fetch_covid_confirmed_cases()

# Extract total confirmed cases for Saskatchewan
    saskatchewan_confirmed_cases = df_confirmed_cases[df_confirmed_cases['Province/State'] == 'Saskatchewan']

# Reset the index
    saskatchewan_confirmed_cases = saskatchewan_confirmed_cases.reset_index(drop=True)

# Dropping the extra columns for further tranformation Province/State','Country/Region', 'Lat', 'Long'
    saskatchewan_confirmed_cases = saskatchewan_confirmed_cases.drop(['Province/State','Country/Region', 'Lat', 'Long'], axis=1)
    saskatchewan_confirmed_cases.reset_index(drop=True, inplace=True)

#Inverting the data making columns as rows
    saskatchewan_confirmed_cases = saskatchewan_confirmed_cases.transpose()

# Adding header to the newly created column
    saskatchewan_confirmed_cases.columns = [ 'SK_Confirmed_Cases']

# Adding header to the Date column 
    saskatchewan_confirmed_cases = saskatchewan_confirmed_cases.rename_axis('Date').reset_index()

    return saskatchewan_confirmed_cases


#Transforming the Saskatchewan death cases
def SaskatchewanCovidDeathCasesData():

  #Calling fetch_covid_confirmed_cases in datLoader to get Global covid confirmed Cases
    df_death_cases = covid_data_loader.fetch_covid_death_cases()  

# Extract total confirmed cases and deaths for Saskatchewan
    saskatchewan_ddata = df_death_cases[df_death_cases['Province/State'] == 'Saskatchewan']

# Reset the index
    saskatchewan_ddata = saskatchewan_ddata.reset_index(drop=True)

# Dropping the extra columns for further tranformation Province/State','Country/Region', 'Lat', 'Long'
    saskatchewan_ddata = saskatchewan_ddata.drop(['Province/State','Country/Region', 'Lat', 'Long'], axis=1)

#Inverting the data making columns as rows
    saskatchewan_ddata = saskatchewan_ddata.transpose()

# Adding header to the newly created column
    saskatchewan_ddata.columns = [ 'SK_Death_Cases']

# Adding header to the Date column 
    saskatchewan_ddata = saskatchewan_ddata.rename_axis('Date').reset_index()

    return saskatchewan_ddata



#Adding dailycases in one dataframe and filtering the dataframe
def SkTotalCovidData():

#Retrieving data from the above methods to add both the cases together
    sk_cc = SaskatchewanCovidConfirmedCasesData()
    sk_dc = SaskatchewanCovidDeathCasesData()

#Merging both datas based on the date column
    new_sk_data = pd.merge(sk_cc, sk_dc, on='Date', how='outer')

#If both the columns has zero value , dropping it
    saskatchewan_ddata_filtered = new_sk_data.loc[~((new_sk_data['SK_Confirmed_Cases'] == 0) & (new_sk_data['SK_Death_Cases'] == 0))]

# Filling NaN values with 0, if any
    saskatchewan_ddata_filtered = saskatchewan_ddata_filtered.fillna(0)

#Reseting the index value
    saskatchewan_ddata_filtered = saskatchewan_ddata_filtered.reset_index(drop=True)

    return saskatchewan_ddata_filtered


