# Step 8: To append data retreived from Stocks API with the Covid data aggregated for all the countries in the World
# Author: Simranbir Kaur
# Student Id: 000490704

import pandas as pd 
import stock_data_loader
import covid_data_analysis

def replace_zeros_with_nearest_nonzero(df):
    mask = df == 0
    df = df.mask(mask).fillna(method='ffill')
    return df.where(~mask, df)

def covidAndStocksData():

    # Calling stock_data_retrieval to get stocks related data for SPG 
    stocks_real_estate_data = stock_data_loader.retrieve_stock_data('SPG')

    # Calling stock_data_retrieval to get stocks related data for DAL 
    stocks_travel_sector_data = stock_data_loader.retrieve_stock_data('DAL')
    
    # Calling global_covid_data_analysis to get coVID aggregated data
    covid_data = covid_data_analysis.aggregateCovidData()

    # Merging Covid Data and stocks_real_estate_data
    results = pd.merge(covid_data, stocks_real_estate_data, on='Date', how='outer').fillna(0)
    # Replace zero values in stock data of SPG with nearest non-zero values from previous rows
    results.iloc[:, 1:] = replace_zeros_with_nearest_nonzero(results.iloc[:, 1:])

    # Merging the above merged results and stocks_travel_sector_data to get the final data
    final_data = pd.merge(results, stocks_travel_sector_data, on='Date', how='outer').fillna(0)
    # Replace zero values in stock data of DAL with nearest non-zero values from previous rows
    final_data.iloc[:, 3:] = replace_zeros_with_nearest_nonzero(final_data.iloc[:, 3:])

    return final_data
    