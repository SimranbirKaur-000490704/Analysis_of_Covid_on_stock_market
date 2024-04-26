# Step 9 b: b)	Create a horizontal bar chart of the top 20 countries according to the confirmed COVID-19 numbers for a given date.
# The bars should be sorted in ascending order. Use a colormap
#Author Dhiraj Kaushal
#Student Id: 000489367

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import covid_data_loader

def millions_formatter(x, pos):
    return f'{int(x/1e6)}M'


def covid_confirmed_cases_visualisation():
    # Fetch confirmed covid cases from fetch_covid_confirmed_cases in dataloader class 
    df = covid_data_loader.fetch_covid_confirmed_cases()

    #Filling value for Province/State as Country/Region where Province/State is NaN
    df['Province/State'].fillna(df['Country/Region'], inplace=True)

    #Grouping 'Country/Region', 'Province/State' and adding the values to get a single sum of cases for countries.
    modified_data_grouping_states = df.groupby(['Country/Region', 'Province/State'], as_index=False).sum(numeric_only=True)
    
    # Extract the last date's data (you can change the date as needed)
    latest_date_data = modified_data_grouping_states[modified_data_grouping_states.columns[-1]]

    # Create a DataFrame with 'Country' and 'ConfirmedCases'
    data = {
        'Country': modified_data_grouping_states['Country/Region'],
        'ConfirmedCases': latest_date_data
    }
    df_confirmed = pd.DataFrame(data)

    # Sort the DataFrame by ConfirmedCases in ascending order
    df_confirmed = df_confirmed.sort_values(by='ConfirmedCases', ascending=True)

    # Select the top 20 countries
    top_20_countries = df_confirmed.tail(20)

    # Plotting the horizontal bar chart
    plt.figure(figsize=(10, 8))
    colors = plt.cm.viridis_r(top_20_countries['ConfirmedCases'] / top_20_countries['ConfirmedCases'].max())  # Using viridis colormap
    bars = plt.barh(top_20_countries['Country'], top_20_countries['ConfirmedCases'], color=colors)

    # Adding labels and title with bold fontweight
    plt.xlabel('Confirmed Cases (in millions)', fontweight='bold')
    plt.ylabel('Country', fontweight='bold')
    plt.title('Top 20 Countries with Confirmed COVID-19 Cases (Latest Date)', fontweight='bold')
    plt.grid(axis='x', linestyle='--', alpha=0.6)

    # Setting x-axis formatter to display numbers in millions
    formatter = ticker.FuncFormatter(millions_formatter)
    plt.gca().xaxis.set_major_formatter(formatter)

    # Adding data labels with specific colors and reduced font size
    for i, (bar, label) in enumerate(zip(bars, top_20_countries['ConfirmedCases'])):
        color = 'white' if i == 19 else 'black'  # White color for the first label, black for the rest
        plt.text(bar.get_width() - (bar.get_width() * 0.03), bar.get_y() + bar.get_height() / 2, f'{label:,}', 
                 ha='right', va='center', color=color, fontsize=9, fontweight='bold')

    plt.show()
