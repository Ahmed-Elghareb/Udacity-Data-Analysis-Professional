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
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # get user input for month (all, january, february, ... , june)


    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]
    months = ["junuary", "february", "march", "april", "may", "june" ,"all" ]
    city = input("Please choose a city to analyze ! :")
    month = input("Please name a month to filter by..if all , please enter all! :").lower()
    day = input("Please enter a day of week to filter by..if all , please enter all! :").lower()
    
    while city not in CITY_DATA.keys() :
         city = input("Please choose a valid city from chicago, washington, and new york city :").lower()
         
    while month not in months :
         month = input("Please choose a valid month from junuary, february, march, april, may, june ,all :").lower()
         
    while day not in days :
         day = input("Please choose a valid week day from monday, tuesday, wednesday, thursday, friday, saturday, sunday, or 'all'! :").lower()
                  
    print('-'*40)
    return city, month, day



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
    months = ["junuary", "february", "march", "april", "may", "june" ,"all" ]

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['months'] = df['Start Time'].dt.month
    df['Week Day'] = df['Start Time'].dt.day_name()
    

    if day != "all":
        df = df[df['Week Day'] == day.title()]
    
    if month != "all":
        month_index = months.index(month) +1
        df = df[df['months'] == month_index]


    return df


# x =load_data('chicago','april','monday')

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    months = ["junuary", "february", "march", "april", "may", "june" ,"all" ]
    start_time = time.time()

    # display the most common month
    popular_month = (df['Start Time'].dt.month).mode()[0]
    popular_month = months[popular_month-1]
    print("The most common start month is :" , popular_month)
    # display the most common day of week
    popular_day = (df['Start Time'].dt.day_name()).mode()[0]
    print("The most common start day is :" , popular_day.title())

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The most common start hour is :" , popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_Sstation = df["Start Station"].mode()[0]
    print("The most common start station is :" , popular_Sstation)

    # display most commonly used end station
    popular_Estation = df["End Station"].mode()[0]
    print("The most common End station is :" , popular_Estation)


    # display most frequent combination of start station and end station trip
    df["Combined Station"]=(df["End Station"]+df["Start Station"])
    popular_comb = df["Combined Station"].mode()[0]
    print("The most common End station is :" , popular_comb)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time= df["Trip Duration"].sum()
    print("The total trip time is, in secs :" , total_time)


    # display mean travel time
    mean_time= df["Trip Duration"].mean()
    print("The total trip time, in secs is :" , mean_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df["User Type"].value_counts()
    print("The counts of user types is :" , user_types[:])


    # Display counts of gender
    try :
        user_gender = df["Gender"].value_counts()
        print("The counts of gender is :" , user_gender)
    except KeyError:
        print("The entered city has no gender data !")
        
        
    # Display earliest, most recent, and most common year of birth
    try :
         earliest_birth = df["Birth Year"].min()
         print("The earliest year of birth is :" , int(earliest_birth))
         recent_birth = df["Birth Year"].max()
         print("The most recent year of birth is :" , int(recent_birth))
         common_birth = df["Birth Year"].mode()[0]
         print("The common year of birth is :" , int(common_birth))
         
    except KeyError:
         print("The entered city has no Birth Year data !")
            
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
  
    
def raw_data(df):
    raw = input('Do you want to have a look on the raw data? Say yes or no : ')
    line_number = 0

    while True:
        if raw.lower() == 'yes':
            print(df.iloc[line_number : line_number + 5])
            line_number += 5
            raw = input('Do you want to see more of the raw data? Enter yes or no.')
        else:
            break    

    
  

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
            break


if __name__ == "__main__":
	main()
