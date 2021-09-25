import time
import datetime
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = {'january':1, 'february':2, 'march':3, 'april':4, 'may':5, 'june':6, 'july':7,
          'august':8, 'september':9, 'october':10,  'november':11, 'december':12,'all':13}

MONTH_DATAinv = {1:'january', 2:'february', 3:'march', 4:'april', 5:'may', 6:'june', 7:'july',
          8:'august', 9:'september', 10:'october',  11:'november', 12:'december',13:'all'}

DAY_DATA =  {'monday':'Monday', 'tuesday':'Tuesday', 'wednesday':'Wednesday', 'thursday':'Thursday', 'friday':'Friday', 'saturday':'Saturday', 'sunday':'Sunday',
          'all':'All'};

def get_filters():
    """
    
    
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    cities = list(CITY_DATA.keys());

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('What city do you want to look at first? ')
    blocker = 1;
    while blocker == 1:
        city = input("City Name:").lower();
        if city != cities[0] and city != cities[1] and city != cities[2]:
            print("Hey, I didn't write a search engine so you are going to need to be more specific.")
        else:
          break
    # TO DO: get user input for month (all, january, february, ... , june)
    month_options = ['january', 'february', 'march', 'april', 'may', 'june', 'july',
          'august', 'september', 'october', 'november', 'december', 'all'];
    valid_months = ['january', 'february', 'march', 'april', 'may', 'june','all']
    while blocker ==1:
        month = input('What month do you want to look at in ' + city + '? ').lower();
        correct_name = 0;
        if month in month_options:
            if month in valid_months:
                correct_name =1;
                break;
            else:
                 correct_name = 2;
        if correct_name == 0:
           print("Hey, I didn't write a search engine so you are going to need to be more specific.");
        elif correct_name == 2:
           print("Unfortunately, we only have data for th first 6 months. Choose again!");
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_options = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday',
          'all'];
    while blocker ==1:
        day = input('What day do you want to look at in ' + city + ' within the month of ' + month + '? ').lower();
        correct_name = 0;
        if day in day_options:
                correct_name =1;
                break;
        if correct_name == 0:
           print("Hey, I didn't write a search engine so you are going to need to be more specific.");
        
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
    cities = list(CITY_DATA.keys());
    
    if city == cities[1]:
                df = pd.read_csv('new_york_city.csv');
                
    elif city == cities[2]:
                df = pd.read_csv('washington.csv');
                
    else:
                df = pd.read_csv('chicago.csv');
            
    start_t = df['Start Time']
    start_month = [int(x[5:7]) for x in start_t];
    start_day = [int(x[8:10]) for x in start_t];
    start_year = [int(x[0:4]) for x in start_t];
    not_matching = []

    if month != 'all':
             
             index = 0;
             for current_month in start_month:                            
                    
                    if MONTH_DATA.get(month) != current_month:
 
                        not_matching.append(index)

                    index += 1;
            
    if day != 'all':
             index = 0;
             for current_day in start_day:
                    day_name = datetime.datetime(start_year[index],start_month[index],start_day[index]).strftime('%A')
                    
                    if DAY_DATA.get(day) != day_name:
                        not_matching.append(index)
                        
                    index += 1;
                    
    df = df.drop(list(set(not_matching)))    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    print(df)
    start_time = time.time()
    start_t = df['Start Time']
    start_month= [int(x[5:7]) for x in start_t];
    start_day= [int(x[8:10]) for x in start_t];
    start_year = [int(x[0:4]) for x in start_t];
    
    # TO DO: display the most common month
    
    MONTH = list(MONTH_DATA.keys());       
    month_ticker = 0;
    most_month = MONTH_DATAinv.get(start_month[0]);

    for i in range(12):
        count = 0;
        
        for current_month in start_month: 
            
                    if i == current_month:
                        count += 1;  
                        
        if month_ticker < count:
            month_ticker = count;
            most_month = MONTH_DATAinv.get(i);
            
    print('the most common month is: '+ most_month)
            
    # TO DO: display the most common day of week
    DAY = list(DAY_DATA.keys());
    day_ticker = 0;
    most_day = datetime.datetime(start_year[0],start_month[0],start_day[0]).strftime('%A')
    
    for i in range(7):
        count = 0;
        index = 0;
        
        for current_day in start_day:
                    day_name = datetime.datetime(start_year[index],start_month[index],start_day[index]).strftime('%A')
                
                    if DAY[i] == current_day:
                        count += 1;    
                        
                    index +=1;
                    
        if day_ticker < count:
            day_ticker = count;
            most_day = DAY[i];

    print('the most common day is: '+ most_day)

    # TO DO: display the most common start hour       
    start_hour= [int(x[12:13]) for x in start_t];
    HOUR = range(len(start_hour)); 
    hour_ticker = 0;
    most_hour = start_hour[0]
    
    for i in range(24):
        count = 0;     
        
        for current_hour in start_hour:                                 
                    if i == start_hour:
                        count += 1;
            
        if hour_ticker < count:
            hour_ticker = count;
            most_hour = HOUR[i];
            
    print('The most common hour is: ' + str(most_hour) + ':00 Military Time')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_st = df['Start Station'];
    start_st = pd.Series(start_st)
    maxstation = str(start_st.value_counts().index[0])

        
    print('The most common start station is: ' + maxstation)
    
    # TO DO: display most commonly used end station
    end_st = df['End Station'];
    end_st = pd.Series(end_st)
    maxstation = str(end_st.value_counts().index[0])
   
    print('The most common end station is: ' + maxstation)
    
        
    # TO DO: display most frequent combination of start station and end station trip
    comb_st = list(map(str.__add__,['from ']*len(start_st),start_st));
    comb_st = list(map(str.__add__,comb_st,[' to ']*len(comb_st)));
    comb_st = list(map(str.__add__,comb_st, end_st));
    comb_st = pd.Series(comb_st)
    maxstation = str(comb_st.value_counts().index[0])
    
    print('The most common route from start station to end station is ' + maxstation)
    

        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    trip_dur = df['Trip Duration']
    total_trip=0;
    # TO DO: display total travel time
    print('The total number of minutes spent biking in this city is: '+str((trip_dur.sum()/60)))
        


    # TO DO: display mean travel time
    print('The average number of minutes spent biking in this city per trip is: '+str(trip_dur.mean()/60))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The number of ' + str(df['User Type'].value_counts().index[0]) + 's is ' + str(df['User Type'].value_counts()[0]))
    print('The number of ' + str(df['User Type'].value_counts().index[1]) + 's is ' + str(df['User Type'].value_counts()[1]))
    

        
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print('The number of ' + str(df['Gender'].value_counts().index[0]) + 's is ' + str(df['Gender'].value_counts()[0]))
        print('The number of ' + str(df['Gender'].value_counts().index[1]) + 's is ' + str(df['Gender'].value_counts()[1]))
        

            
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('The earliest birth year is: '+ str(int(df['Birth Year'].min())))
        print('The most recent birth year is: ' + str(int(df['Birth Year'].max())))
        print('The most common birth year is: ' + str(int(df['Birth Year'].value_counts().index[0])))

            
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """ Display the data selected by the user before any statistics (The structure of the following function was taken from a suggested structure from initial Udacity Review)"""
    i = 5
    raw = input("Would you like to take a look at the data you have chosen?") # TO DO: convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',50)

    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df.head(i)) # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw = input("Would you like to see more of the data?") # TO DO: convert the user input to lower case using lower() function
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
