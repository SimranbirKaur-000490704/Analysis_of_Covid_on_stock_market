# Step 2 of Final Project: data_loader.py file loads data from different urls, it contains methods for achieving the same
# Author: Simranbir Kaur
# Student Id: 000490704

import pandas as pd
import constant

#method that loads data from covid confirmed cases url
def fetch_covid_confirmed_cases():
    df_confirmed_cases = pd.read_csv(constant.COVID_CONFIRMED_CASES_URL)

    # Save the DataFrame to a CSV file
    df_confirmed_cases.to_csv('data_csv/covid/covid_confirmed_cases.csv', index=False)

    #Returning the dataframe of covid confirmed cases
    return df_confirmed_cases

#method that loads data from covid death cases url
def fetch_covid_death_cases():
    df_death_cases = pd.read_csv(constant.COVID_DEATHS_CASES_URL)

     # Save the DataFrame to a CSV file
    df_death_cases.to_csv('data_csv/covid/covid_death_cases.csv', index=False)

    #Returning the dataframe of covid death cases
    return df_death_cases