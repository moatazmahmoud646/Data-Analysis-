import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington':'washington.csv' }

dict1={}
for key in CITY_DATA:
    dict1[key.replace(' ', '')]=CITY_DATA[key]
def get_filters():
    m=['january', 'february', 'march', 'april', 'may', 'june']
    d=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    while True:
        city=input("Enter city name:chicago, new york city, washington ")
        month=input("Enter month:all, january, february, ... , june ")
        day=input("Enter day all, monday, tuesday, ... sunday ") 
        if city.lower().strip().replace(" ", "") not in dict1:
            print("PLEASE ENTER VALID CITY NAME")
            
    
        if month.lower() not in m:
            print("PLEASE ENTER VALID MONTH")
        if day.lower() not in d:
            print("PLEASE ENTER VALID DAY")
        else:
            break
    
    print('Hello! Let\'s explore some US bikeshare data!')
    

    print('_'*40)
    return city.lower(), month.lower(), day.lower()


def load_data(city, month, day):
    
        df = pd.read_csv(CITY_DATA[city])
        df['Start Time']=pd.to_datetime(df['Start Time'])
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.day_name()
        df['hour']=df['Start Time'].dt.hour
        if month!='all':
            m=['january', 'february', 'march', 'april', 'may', 'june']
            month=m.index(month)+1
            df=df[df['month']==month]
        if day != 'all': 
            df = df[df['day_of_week'] == day.title()]
    
         
         
       
        return df



def time_stats(df):

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print("the most common month",df['month'].mode()[0])

    print("the most common day",df['day_of_week'].mode()[0])


    print("the most common hour",df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print("most commonly used start station : ",df['Start Station'].mode())

    print("most commonly used end station : ",df['End Station'].mode())


    print(" most frequent combination of start station and end station trip : ",df.groupby('Start Station')['End Station'].value_counts().idxmax())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print('total travel time : ',df['Trip Duration'].sum())

    print('mean travel time : ',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print('counts of user types : ',df['User Type'].value_counts())
    
    if  'Gender'  in df:
        print(' counts of gender : ',df['Gender'].value_counts())
    if  'Birth Year'  in df:
        print('earliest, most recent, and most common year of birth : ',df['Birth Year'].min(),df['Birth Year'].max(),df['Birth Year'].mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display(df):
  pd.set_option("display.max_columns", None)
  i=0
  z=5
  while True:
      
      y=df.iloc[i:z]
      i+=5
      z+=5
      print(y)
      user=input('\ DO YOU WANT TO DISPLAY MORE ROWS')
      if user.lower() != 'yes':
          break
  
    
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        display(df)
          
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
