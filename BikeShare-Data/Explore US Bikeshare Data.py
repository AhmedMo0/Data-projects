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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    global city
    global month
    global day
    
    city = input("choose a country! Chicago, New York City, Washington : ")
    
    
    while ( (city != "Chicago") and (city != "New York City") and  (city != "Washington") ):
        city = input("choose a valid country! Chicago, New York or Washington : ")
    
   
    # TO DO: get user input for month (all, january, february, ... , june)
    
    months_l = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December', 'All']
    
    month = input("Type a full month name (all, january, february, ... ) : ")
    
    
    while(month.capitalize() not in months_l):
                month = input("Type a full month name correctly (january, february, ... ) : ")
    
                

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday","All")
    
    day = input("Type a full day name (all, monday, tuesday, ...) : ")
    
    while(day.capitalize() not in weekDays):
                day = input("Type a full day name correctly (monday, tuesday, ...) : ")
     

    print('-'*40)
                            
    return  city,  month,  day


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
    df = pd.read_csv(CITY_DATA[city.lower()])
    dt = df["Start Time"]
    STimeList = df["Start Time"]
    STimeList = pd.to_datetime(STimeList)
                
    #start filtering
    
    if(month != "all" and day != "all"):
        # filter according to months
        months = STimeList.dt.month_name()
        month_ok = months == month.capitalize()
        month_list = dt[month_ok].tolist()
                            
        fltrd_list = df["Start Time"].isin(month_list)
        fltrd = df[fltrd_list]
        df = fltrd
        fltrd = fltrd["Start Time"]
        fltrd = pd.to_datetime(fltrd)
        
        
                            
        # Then filter according to days 
        days = fltrd.dt.day_name()
        day_ok = days == day.capitalize()
        day_list = df["Start Time"][day_ok].tolist()
        
        
        fltrd_list = df["Start Time"].isin(day_list)
        fltrd = df[fltrd_list]    
        df = fltrd
         
                            
    elif(month != "all"):
                            
        months = STimeList.dt.month_name()
        month_ok = months == month.capitalize()
        month_list = dt[month_ok].tolist()
                            
        fltrd_list = df["Start Time"].isin(month_list)
        fltrd = df[fltrd_list]
        df = fltrd
                            
                            
    elif(day != "all"):
                            
        days = fltrd.dt.day_name()
        day_ok = days == day.capitalize()
        day_list = df["Start Time"][day_ok].tolist()
        
        
        fltrd_list = df["Start Time"].isin(day_list)
        fltrd = df[fltrd_list]    
        df = fltrd
                           
                
    
     
         
    
    
    


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
                            
    if(month == "all"):
        comm = df["Start Time"]
        com_month = pd.to_datetime(comm)
        com_month = com_month.dt.month_name()
        com_month = com_month.mode()
        print("common month --> " + com_month.iloc[0])
                            
                            
                          

    # TO DO: display the most common day of week
                            
    if(day == "all"):
        comd = df["Start Time"]
        com_day = pd.to_datetime(comd)
        com_day = com_day.dt.day_name()
        com_day = com_day.mode()
        print("common day --> " + com_day.iloc[0])
                            
                            


    # TO DO: display the most common start hour
    d_time = pd.to_datetime(df["Start Time"]) 
    hr = d_time.dt.hour
    hr = hr.value_counts()
    pup_h = hr.index[0]
    h_count = hr.iloc[0]
    print("popular hour --> " ,end="" )
    print(pup_h)
    print(" count: " ,end="")
    print(h_count)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    CS_station = df["Start Station"].mode()
    print("most commonly used start station --> " + CS_station[0])
                            

    # TO DO: display most commonly used end station

    CE_station = df["End Station"].mode()
    print("most commonly used End station --> " + CE_station[0])

                            
    # TO DO: display most frequent combination of start station and end station trip

    trip = df[["Start Station", "End Station"]].copy()
    p_trip = trip.mode().iloc[0]
    print(p_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    ttt = df["Trip Duration"].sum()
    print("total time travel --> ", end="")
    print(ttt)


    # TO DO: display mean travel time
    # total time avrage
    trip_count = df["Trip Duration"].count()
    tta = ttt/trip_count
    print("total time avrage --> ", end="")
    print(tta)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    usert_count = df["User Type"].value_counts()
    print("counts of user types --> " ,end="")
    print(usert_count)


    # TO DO: Display counts of gender
    
    if(city == "Washington"):
        print("No available data to share")

    else:                        
        gender_count = df["Gender"].value_counts()
        print("gender count:")
        print(gender_count)


    # TO DO: Display earliest, most recent, and most common year of birth
    if(city == "Washington"):
        print("No available data to share")

    else:
        max_y = df["Birth Year"].max()
        min_y = df["Birth Year"].min()
        p_y = df["Birth Year"].mode().iloc[0]
        print("earliest year of birth --> " , end="")
        print(max_y)
        print("most recent year of birth --> " , end="")
        print(min_y)
        print("most common year of birth --> " , end="")
        print(p_y)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def view_sample(state,df):
    
    
    count = 0
    while state.lower() == "yes":
        print("")
        print(df.iloc[count:count+5])
        count += 5
        state = input("Do you wish to continue?: ")
        
        
    
    
    
    
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        Qu = input("\nWould you like to view 5 rows of individual trip data? Enter yes or no : ")
        
        view_sample(Qu,df)
        
        
       
            
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
