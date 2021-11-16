#Date - time
#Import Python's datetime module
import datetime

#import date class from datetime module
from datetime import date

#Assing today's date to the variable today
today = date.today()

#Print the date today
print(f"Today is year {today.year}, month {today.month}, date {today.day}.")
