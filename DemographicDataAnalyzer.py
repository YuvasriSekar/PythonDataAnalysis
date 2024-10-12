import pandas as pd

# Function to load the dataset
def load_data():
    # Assuming the CSV file is named 'adult.data.csv'
    df = pd.read_csv('adult.data.csv', header=None)
    
    # Assign column names based on the dataset description
    df.columns = ['age', 'workclass', 'fnlwgt', 'education', 'education-num',
                  'marital-status', 'occupation', 'relationship', 'race', 
                  'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 
                  'native-country', 'salary']
    
    return df

# Function to calculate race count
def race_count(df):
    return df['race'].value_counts()

# Function to calculate average age of men
def average_age_men(df):
    return df[df['sex'] == 'Male']['age'].mean().round(1)

# Function to calculate the percentage of people with a Bachelor's degree
def percentage_bachelors(df):
    total = len(df)
    bachelors = len(df[df['education'] == 'Bachelors'])
    return (bachelors / total * 100).round(1)

# Function to calculate the percentage of people with advanced education making >50K
def advanced_education_percentage(df):
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    high_income = df['salary'] == '>50K'
    
    advanced_high_income = df[advanced_education & high_income]
    total_advanced = df[advanced_education]
    
    return (len(advanced_high_income) / len(total_advanced) * 100).round(1)

# Function to calculate the percentage of people without advanced education making >50K
def non_advanced_education_percentage(df):
    non_advanced_education = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    high_income = df['salary'] == '>50K'
    
    non_advanced_high_income = df[non_advanced_education & high_income]
    total_non_advanced = df[non_advanced_education]
    
    return (len(non_advanced_high_income) / len(total_non_advanced) * 100).round(1)

# Function to calculate minimum work hours
def min_work_hours(df):
    return df['hours-per-week'].min()

# Function to calculate the percentage of people working minimum hours and earning >50K
def percentage_min_hours_high_income(df):
    min_hours = df['hours-per-week'].min()
    min_hour_workers = df[df['hours-per-week'] == min_hours]
    
    high_income_min_workers = min_hour_workers[min_hour_workers['salary'] == '>50K']
    
    return (len(high_income_min_workers) / len(min_hour_workers) * 100).round(1)

# Function to calculate the country with the highest percentage of people earning >50K
def highest_earning_country(df):
    country_earnings = df[df['salary'] == '>50K'].groupby('native-country').size()
    country_totals = df.groupby('native-country').size()
    
    highest_country = (country_earnings / country_totals * 100).idxmax()
    highest_percentage = (country_earnings / country_totals * 100).max().round(1)
    
    return highest_country, highest_percentage

# Function to find the most popular occupation for people earning >50K in India
def top_occupation_india(df):
    india_high_income = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    
    return india_high_income['occupation'].value_counts().idxmax()

# Main function to print the analysis results
if __name__ == "__main__":
    df = load_data()

    print("Race count:\n", race_count(df))
    print("Average age of men:", average_age_men(df))
    print("Percentage with Bachelors degrees:", percentage_bachelors(df))
    print("Percentage with advanced education making >50K:", advanced_education_percentage(df))
    print("Percentage without advanced education making >50K:", non_advanced_education_percentage(df))
    print("Min work hours:", min_work_hours(df))
    print("Percentage of people working min hours and earning >50K:", percentage_min_hours_high_income(df))
    
    country, percentage = highest_earning_country(df)
    print(f"Highest earning country: {country} with {percentage}%")
    
    print("Most popular occupation for >50K earners in India:", top_occupation_india(df))
