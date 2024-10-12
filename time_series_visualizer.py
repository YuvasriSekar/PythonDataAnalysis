import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from "fcc-forum-pageviews.csv"
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean the data
df = df[
    (df['value'] <= df['value'].quantile(0.975)) &
    (df['value'] >= df['value'].quantile(0.025))
]

def draw_line_plot():
    # Create a line plot
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['value'], color='blue', linewidth=2)
    
    # Title and labels
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    
    # Save the figure
    plt.savefig('line_plot.png')
    plt.show()

def draw_bar_plot():
    # Prepare data for bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    
    # Group by year and month
    df_bar_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Draw bar plot
    plt.figure(figsize=(10, 6))
    df_bar_grouped.plot(kind='bar', legend=True)
    
    # Title and labels
    plt.title('Average Daily Page Views per Month')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.xticks(rotation=45)
    plt.legend(title='Months')
    
    # Save the figure
    plt.savefig('bar_plot.png')
    plt.show()

def draw_box_plot():
    # Prepare data for box plot
    df_box = df.copy()
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.month

    # Draw box plots
    plt.figure(figsize=(12, 6))
    
    # Year-wise box plot
    plt.subplot(1, 2, 1)
    sns.boxplot(x='year', y='value', data=df_box)
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    
    # Month-wise box plot
    plt.subplot(1, 2, 2)
    sns.boxplot(x='month', y='value', data=df_box, order=[
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ])
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    
    # Save the figure
    plt.savefig('box_plot.png')
    plt.show()

# Call the functions to create the plots
if __name__ == "__main__":
    draw_line_plot()
    draw_bar_plot()
    draw_box_plot()
