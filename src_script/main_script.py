# main.py is the main script file of this project whcih is the start point of this project
# Author: Simranbir Kaur
# Student Id: 000490704

import covid_data_analysis
import covid_SK_data
import covid_datewise_data
import pandas as pd
import stock_data_analysis
import covid_stocks_graph
import covid_countries_graph

#Calling Data Dictionary to hold date wise covid Data and saving its output to date_wise_covid_data.csv file
date_wise_covid_data = covid_datewise_data.generate_datewise_dataframe()
print("date wise covid data of all countries",date_wise_covid_data)     

# Fetching Saskatchewan Filtered Covid Cases and saving its output to saskatchewan_data.csv
saskatchewan_data = covid_SK_data.SkTotalCovidData()
saskatchewan_data.to_csv('data_csv/output/saskatchewan_data.csv', index=True)

# Total aggregated Covid data and 2 stocks data in one dataframe and save its output to total_covid_Stock_data.csv file
total_covid_Stock_data = stock_data_analysis.covidAndStocksData()
total_covid_Stock_data.to_csv('data_csv/output/total_covid_Stock_data.csv', index=True)

# To get visualization stocks in relation to covid data
covid_stocks_graph.StocksDataInRelationToCovidDataGraph(total_covid_Stock_data)

# To get visualization of confirmed covid cases of top 20 countries
covid_countries_graph.covid_confirmed_cases_visualisation()
