import pandas as pd
import numpy as np

def analyze_demographic_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)

    # How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()
    
    #Bachelor degree
    percentage_bachelors = ((df['education'] == 'Bachelors').mean()) * 100

    # Advanced education filters
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    
    # What percentage of people with advanced education make more than 50K?
    higher_education_rich = ((df[advanced_education]['salary'] == '>50K').mean()) * 100

    # What percentage of people without advanced education make more than 50K?
    lower_education_rich = ((df[~advanced_education]['salary'] == '>50K').mean()) * 100

    # What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = ((num_min_workers['salary'] == '>50K').mean()) * 100

    # What country has the highest percentage of people that earn >50K?
    country_earn_over_50K_ratio = df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()
    highest_earning_country = country_earn_over_50K_ratio.idxmax()
    highest_earning_country_percentage = country_earn_over_50K_ratio.max() * 100

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    # Print the results
    print(f"Number of people by race:\n{race_count}\n")
    print(f"Average age of men: {average_age_men}\n")
    print(f"Percentage with Bachelors degrees: {percentage_bachelors}%\n")
    print(f"Percentage with higher education that earn >50K: {higher_education_rich}%\n")
    print(f"Percentage without higher education that earn >50K: {lower_education_rich}%\n")
    print(f"Min work hours: {min_work_hours}\n")
    print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%\n")
    print(f"Country with highest percentage of rich: {highest_earning_country} with {highest_earning_country_percentage}%\n")
    print(f"Top occupation in India among those who earn >50K: {top_IN_occupation}\n")

# Assuming the file is named 'data.csv' and located in the same directory as this script.
file_path = 'data.csv'
analyze_demographic_data(file_path)
