# Python Project 
# Date: Mon March 29th, 2021

# In this project, you will use data provided by Motivate, a bike share system provider for many major cities in the United States, 
# to uncover bike share usage patterns. You will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\n Hello! Let\'s explore some US bikeshare data! \n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_filter = input("\n Would you like to see data for Chicago, New York City, or Washington? \n").title()
    while city_filter not in ['Chicago', 'New York City', 'Washington']:
        city_filter = input("\n The name of the city is incorrect. Would you like to see data for Chicago, New York City, or Washington? \n").title()

    # TO DO: get user input for month (all, january, february, ... , june)
    month_filter = input('\n For which month would you like to filter the data? January , February, March, April, June? Type "All" for no time filter \n').title()
    while month_filter != 'January' and month_filter != 'February' and month_filter != 'March' and month_filter != 'April' and month_filter != 'May' and month_filter != 'June' and month_filter != 'All':
        month_filter = input('\n For which month would you like to filter the data? January , February, March, April, June? Type "All" for no time filter \n').title()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_filter = input('\n For which day would you like to filter the data? Type "All" for no time filter \n').title()
    while day_filter != 'Monday' and day_filter != 'Tuesday' and day_filter != 'Wednesday' and day_filter != 'Thursday' and day_filter != 'Friday' and day_filter != 'Saturday' and day_filter != 'Sunday' and day_filter != 'All':
        day_filter = input('\n It is wrong written. For which day would you like to filter the data? Type "All" for no time filter \n').title()

    print('-'*40)
    return city_filter, month_filter, day_filter


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
     # load data file into a dataframe
    df = pd.DataFrame(pd.read_csv(CITY_DATA[city]))

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('\n Most common month: ', common_month, '\n')
    
    
    # TO DO: display the most common day of week
    df['day_week'] = df['Start Time'].dt.weekday_name
    common_day_week = df['day_week'].mode()[0]
    print('\n Most common day of week: ', common_day_week, '\n')

    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print('\n Most common start hour:', common_start_hour, '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('\n Most common start station: ', common_start_station, '\n')


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('\n Most common end station: ', common_end_station, '\n')


    # TO DO: display most frequent combination of start station and end station trip
    df['common_start_end_station'] = df['Start Station'] + df['End Station']
    common_start_end_station = df['common_start_end_station'].mode()[0]
    print('\n Most frequent combination of start station and end station trip: ', common_start_end_station, '\n')
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('\n Total travel time: ', total_travel, '\n')
    
    
    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('\n Mean travel time: ', mean_travel, '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    # TO DO: Display counts of user types
    user_counts = df['User Type'].value_counts()
    print('\n What is the breakdown of users?: \n', user_counts)


    # TO DO: Display counts of gender
    if city != 'Washington':
        gender_counts = df['Gender'].value_counts()
        print('\n What is the breakdown of gender?: \n', gender_counts)


    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'Washington':
        oldest = df['Birth Year'].max()
        youngest = df['Birth Year'].min()
        popular_birth = df['Birth Year'].mode()[0]
        print('\n What is the oldest, youngest, and most popular year of birth, respectively? \n', oldest, youngest, popular_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        
        show_data = input("\n Would you like to see 5 lines of data? \n").lower()
        i = 0
        while show_data == 'yes':
            print(df.iloc[i:i+5, :])
            show_data = input("\n Would you like to see 5 lines of data? \n").lower()
            i += 5
            
        
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
