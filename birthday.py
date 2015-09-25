"""
birthday.py
Author: Anoushka Alavilli
Credit: Sarah Dunbar, Jasmine Lou, Mr. Dennison, JC Napier
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = str(datetime.today().day)
tmonth= month_name[todaymonth]

name= input("Hello, what is your name? ")
month= input("Hi {0}, what was the name of the month you were born in? ".format(name))
year= input("And what year were you born in, {0}? ".format(name))
day= input("And the day? ")
yearint=int(year)
if tmonth==month and todaydate==day:
    print ("Happy birthday!")
    
elif month=="October" and day=="31":
    print ("You were born on Halloween!")
else:
    if month== "December" or month== "January" or month== "February":
        season="winter"
    if month== "March" or month== "April" or month== "May":
        season="spring"
    if month== "June" or month== "July" or month== "August":
        season="summer"
    if month== "September" or month== "October" or month== "November":
        season="fall"
    if (yearint)>= 1980 and yearint<=1989:
        timeperiod="eighties"
    if (yearint)>= 1990 and yearint<=1999:
        timeperiod="nineties"
    if (yearint)>= 2000 and yearint<=2015:
        timeperiod="two thousands"
    if (yearint)<=1979:
        timeperiod="stone age"
    print (str(name) + ", you are a " + str(season) + " baby of the " + timeperiod)