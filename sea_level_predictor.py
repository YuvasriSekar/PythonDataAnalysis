import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load the data from "epa-sea-level.csv"
df = pd.read_csv('epa-sea-level.csv')

def draw_scatter_plot():
    # Create a scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data Points')

    # Create first line of best fit using all data
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    sea_level_fit = slope * years_extended + intercept
    plt.plot(years_extended, sea_level_fit, color='red', label='Best Fit Line (All Data)')

    # Create second line of best fit using data from year 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    sea_level_fit_recent = slope_recent * years_extended + intercept_recent
    plt.plot(years_extended, sea_level_fit_recent, color='green', label='Best Fit Line (2000 Onwards)')

    # Title and labels
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()

    # Save the figure
    plt.savefig('sea_level_plot.png')
    plt.show()

# Call the function to create the scatter plot
if __name__ == "__main__":
    draw_scatter_plot()
