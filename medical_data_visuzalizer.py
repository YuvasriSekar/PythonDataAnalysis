import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data from medical_examination.csv
df = pd.read_csv('medical_examination.csv')

# Create the overweight column
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2)).apply(lambda x: 1 if x > 25 else 0)

# Normalize cholesterol and gluc columns
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

def draw_cat_plot():
    # Create DataFrame for cat plot
    df_cat = pd.melt(df, id_vars='cardio', value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
    # Group and reformat the data
    df_cat = df_cat.groupby(['cardio', 'variable']).value_counts().reset_index(name='total')
    
    # Draw the categorical plot
    fig = sns.catplot(x='variable', hue='value', col='cardio',
                      data=df_cat, kind='count', height=5, aspect=1.2)
    plt.title('Categorical Plot')
    
    return fig

def draw_heat_map():
    # Clean the data for heatmap
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                  (df['height'] >= df['height'].quantile(0.025)) &
                  (df['height'] <= df['height'].quantile(0.975)) &
                  (df['weight'] >= df['weight'].quantile(0.025)) &
                  (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    plt.figure(figsize=(10, 8))

    # Draw the heatmap
    sns.heatmap(corr, mask=mask, cmap='coolwarm', annot=True, fmt='.1f', linewidths=0.5)

    plt.title('Correlation Heatmap')
    plt.show()

# This is the main entry point for testing purposes
if __name__ == "__main__":
    draw_cat_plot()
    draw_heat_map()
