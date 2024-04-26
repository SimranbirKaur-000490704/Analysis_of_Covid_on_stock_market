#  Step 9 a): For the year 2022, create an appropriate graph(s) that shows the effect of COVID-19 on selected stock prices.
#  Highlight on the graph if you notice any sharp change while comparing values. Consider the data range when you are comparing values in the graph.
#  Explain why you chose the graph(s).
#  You may use Matplotlib, Seaborn or Plotly library for graphs. 
#  Author: Sagar Umeshkumar Patel (Student ID: 000491515)

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import stock_data_analysis
import numpy as np
import matplotlib.dates as mdates
import seaborn as sns

def normalize_data(df):
    # Set which columns to normalize, excluding 'Date'
    columns_to_normalize = df.columns.difference(['Date'])
    scaler = MinMaxScaler()
    df_normalized = df.copy()
    df_normalized[columns_to_normalize] = scaler.fit_transform(df_normalized[columns_to_normalize])
    return df_normalized

def StocksDataInRelationToCovidDataGraph(final_data):
    final_data['Date'] = pd.to_datetime(final_data['Date'])

    # Filter data for Wednesdays in 2022
    data_2022 = final_data[(final_data['Date'].dt.year == 2022) & (final_data['Date'].dt.weekday == 2)]

    # Normalize the data
    data_normalized = normalize_data(data_2022)

    # Printing the normalized data
    print(data_normalized)

    # Create a figure with specified size
    plt.figure(figsize=(15, 7))

    # Plot normalized SPG Prices
    plt.plot(data_normalized['Date'], data_normalized['SPG_Closed_Prices'], label='SPG Prices', color='blue')

    # Plot normalized DAL Prices
    plt.plot(data_normalized['Date'], data_normalized['DAL_Closed_Prices'], label='DAL Prices', color='orange')

    # Plot normalized Confirmed Cases and Death Cases
    plt.plot(data_normalized['Date'], data_normalized['Confirmed_Cases'], label='Confirmed Cases', color='green', linestyle='--')
    plt.plot(data_normalized['Date'], data_normalized['Death_Cases'], label='Death Cases', color='red', linestyle='--')

    # Find and plot highest and lowest points for SPG
    highest_spg = data_normalized['SPG_Closed_Prices'].idxmax()
    lowest_spg = data_normalized['SPG_Closed_Prices'].idxmin()
    biggest_change_spg = data_normalized['SPG_Closed_Prices'].diff().abs().idxmax()

    # Plotting highest SPG price point
    plt.scatter(data_normalized.loc[highest_spg, 'Date'], data_normalized.loc[highest_spg, 'SPG_Closed_Prices'],
        color='green', marker='o', s=100, label='Highest SPG Price')
    plt.annotate(f'Price: {data_normalized.loc[highest_spg, "SPG_Closed_Prices"]:.2f}',
        (data_normalized.loc[highest_spg, 'Date'], data_normalized.loc[highest_spg, 'SPG_Closed_Prices']),
        textcoords="offset points", xytext=(10,5), ha='left', fontsize=10, color='black', fontweight='bold')

    # Plotting lowest SPG price point
    plt.scatter(data_normalized.loc[lowest_spg, 'Date'], data_normalized.loc[lowest_spg, 'SPG_Closed_Prices'],
        color='purple', marker='o', s=100, label='Lowest SPG Price')
    plt.annotate(f'Price: {data_normalized.loc[lowest_spg, "SPG_Closed_Prices"]:.2f}',
        (data_normalized.loc[lowest_spg, 'Date'], data_normalized.loc[lowest_spg, 'SPG_Closed_Prices']),
        textcoords="offset points", xytext=(10,-10), ha='left', fontsize=10, color='black', fontweight='bold')

    # Plotting biggest change in SPG price point
    plt.scatter(data_normalized.loc[biggest_change_spg, 'Date'], data_normalized.loc[biggest_change_spg, 'SPG_Closed_Prices'],
        color='blue', marker='o', s=100, label='Biggest Change in SPG Price')
    plt.annotate(f'Price: {data_normalized.loc[biggest_change_spg, "SPG_Closed_Prices"]:.2f}',
        (data_normalized.loc[biggest_change_spg, 'Date'], data_normalized.loc[biggest_change_spg, 'SPG_Closed_Prices']),
        textcoords="offset points", xytext=(5,10), ha='left', fontsize=10, color='black', fontweight='bold')

    # Find and plot highest and lowest points for DAL
    highest_dal = data_normalized['DAL_Closed_Prices'].idxmax()
    lowest_dal = data_normalized['DAL_Closed_Prices'].idxmin()
    biggest_change_dal = data_normalized['DAL_Closed_Prices'].diff().abs().idxmax()

    # Plotting highest DAL price point
    plt.scatter(data_normalized.loc[highest_dal, 'Date'], data_normalized.loc[highest_dal, 'DAL_Closed_Prices'],
        color='orange', marker='o', s=100, label='Highest DAL Price')
    plt.annotate(f'Price: {data_normalized.loc[highest_dal, "DAL_Closed_Prices"]:.2f}',
        (data_normalized.loc[highest_dal, 'Date'], data_normalized.loc[highest_dal, 'DAL_Closed_Prices']),
        textcoords="offset points", xytext=(-15,7), ha='left', fontsize=10, color='black', fontweight='bold')

    # Plotting lowest DAL price point
    plt.scatter(data_normalized.loc[lowest_dal, 'Date'], data_normalized.loc[lowest_dal, 'DAL_Closed_Prices'],
        color='red', marker='o', s=100, label='Lowest DAL Price')
    plt.annotate(f'Price: {data_normalized.loc[lowest_dal, "DAL_Closed_Prices"]:.2f}',
        (data_normalized.loc[lowest_dal, 'Date'], data_normalized.loc[lowest_dal, 'DAL_Closed_Prices']),
        textcoords="offset points", xytext=(-10,-10), ha='right', fontsize=10, color='black', fontweight='bold')

    # Plotting biggest change in DAL price point
    plt.scatter(data_normalized.loc[biggest_change_dal, 'Date'], data_normalized.loc[biggest_change_dal, 'DAL_Closed_Prices'],
        color='brown', marker='o', s=100, label='Biggest Change in DAL Price')
    plt.annotate(f'Price: {data_normalized.loc[biggest_change_dal, "DAL_Closed_Prices"]:.2f}',
        (data_normalized.loc[biggest_change_dal, 'Date'], data_normalized.loc[biggest_change_dal, 'DAL_Closed_Prices']),
        textcoords="offset points", xytext=(-10,10), ha='left', fontsize=10, color='black', fontweight='bold')

    # Formatting
    # Set title
    plt.title('Effect of COVID-19 on SPG and DAL Stock Prices in 2022', fontsize=16, fontweight='bold')
    # Set x-label
    plt.xlabel('Dates', fontsize=12, fontweight='bold')
    # Set y-label
    plt.ylabel('Normalized Values', fontsize=12, fontweight='bold')
    # Move legend outside and remove border
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), frameon=False)
    # Enable grid 
    plt.grid(True)

    # Generate date ticks
    date_ticks = np.arange(data_normalized['Date'].min(), data_normalized['Date'].max(), np.timedelta64(7, 'D'))
    # Set x-axis ticks and labels
    plt.xticks(date_ticks, labels=[str(date) for date in date_ticks], rotation=90)
    # 45 ticks
    xticks = data_normalized['Date'].iloc[::len(data_normalized) // 45]
    # Rotate x-axis labels by 90 degrees
    plt.xticks(rotation=90)

    # Customize x-axis ticks and labels (show only date without timestamp)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=7))  # Adjust interval as needed

    # Set the x-axis and y-axis limit to start from 0
    plt.xlim(data_normalized['Date'].min(), data_normalized['Date'].max())
    plt.ylim(-0.05, data_normalized['DAL_Closed_Prices'].max() * 1.05)

    # Set Seaborn theme
    sns.set_theme(style="darkgrid", palette="deep")
    # Adjust plot layout
    plt.tight_layout()
    # Show the plot
    plt.show()
