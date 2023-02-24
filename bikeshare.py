import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    while True:
      city = input("\nKindly select a city to filter data? Chicago, New York City, Washington?\n")
      if city.lower() not in ('new york city', 'chicago', 'washington'):
        print("Sorry. Try again.")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
      month = input("\nKindly select a month to filter data?(january, february, march, april, may, june, all?\n") 
      if month.lower() not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
        print("Sorry. Try again")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
      day = input("\nWhat is the day to filter by?\n")
      if day.lower() not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
        print("Sorry. Try again.")
        continue
      else:
        break

    print('-'*40)
    return city.lower(), month.lower(), day.lower()


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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        MONTH_DATA = ['january', 'february', 'march', 'april', 'may', 'june']
   	 	# use the index of the months list to get the corresponding int
        month = MONTH_DATA.index(month) + 1

    	# filter by month to create the new dataframe
        df = df[df['month'] == month]
        
        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    common_month = df['month'].mode()[0]
    print('The Most Common Month:', common_month)


    # TO DO: display the most common day of week

    common_day = df['day_of_week'].mode()[0]
    print('The Most Common day of Week:', common_day)



    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The Most Common Start Hour:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    Common_Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly Used Start Station:', Common_Start_Station)


    # TO DO: display most commonly used end station

    Common_End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station:', Common_End_Station)


    # TO DO: display most frequent combination of start station and end station trip

    Frequent_Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly Used Combination of Start Station and End Station Trip:', Frequent_Combination_Station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time:', Total_Travel_Time/86400, " Days")


    # TO DO: display mean travel time

    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time/60, " Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)
    
    try:
        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print("The count of user gender is: \n" + str(gender))
        
        # TO DO: Display earliest, most recent, and most common year of birth
        Earliest_Birth = df['Birth Year'].min()
        Most_Recent_Birth = df['Birth Year'].max()
        Most_Common_Birth = df['Birth Year'].mode()[0]
        print('\nEarliest Birth:', Earliest_Birth)
        print('\nMost Recent Birth:', Most_Recent_Birth)
        print('\nMost Common Birth:', Most_Common_Birth)    
    except KeyError:
        print('Washington does not have Gender or Birth Year' )
  
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            return

def raw_data(df):
        first = 0
        while True:
            displayData = input('Would you like to see raw data? yes or no. \n')
            if displayData.lower() != 'yes':
                return
            
            print(df.iloc[first:first+5])
            first = first + 5
            
        


if __name__ == "__main__":
	main()
