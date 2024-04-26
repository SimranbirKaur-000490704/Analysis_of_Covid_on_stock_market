# Step 6 to Step 7: Extracting data for two stocls from ALpha Vantage API
#Author Dhiraj Kaushal
#Student Id: 000489367

import requests
import pandas as pd
import constant

# Function to retrieve stock data and create DataFrame
def retrieve_stock_data(symbol):

    start_date = '2020-01-22'
    end_date = '2023-03-09'


    if symbol == 'SPG':
       url = constant.ALPHA_VANTAGE_URL_REAL_ESTATE
    else:
        url = constant.ALPHA_VANTAGE_URL_TRAVEL_SECTOR


    response = requests.get(url)
    data = response.json()

    # Filter data based on the specified date range
    filtered_dates = [date for date in data['Time Series (Daily)'].keys() if start_date <= date <= end_date]
    high_prices = [float(data['Time Series (Daily)'][date]['2. high']) for date in filtered_dates]
    low_prices = [float(data['Time Series (Daily)'][date]['3. low']) for date in filtered_dates]
    closed_prices = [float(data['Time Series (Daily)'][date]['4. close']) for date in filtered_dates]

    # Create a DataFrame

    if symbol == 'SPG':
        stock_df = pd.DataFrame({'Date': filtered_dates, 
            'SPG_High_Prices': high_prices, 
            'SPG_Low_Prices': low_prices,
            'SPG_Closed_Prices': closed_prices})
        
        stock_df.to_csv('data_csv/stocks/spg_stock_data.csv', index=True)

    else:
        stock_df = pd.DataFrame({'Date': filtered_dates, 
            'DAL_High_Prices': high_prices, 
            'DAL_Low_Prices': low_prices,
            'DAL_Closed_Prices': closed_prices})
        
        stock_df.to_csv('data_csv/stocks/dal_stock_data.csv', index=True)

    return stock_df