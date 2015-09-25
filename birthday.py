"""
birthday.py
Author: Anoushka Alavilli
Credit: Sarah Dunbar, Jasmine Lou, Mr. Dennison
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

name= input("Hello, what is your name?")
month= input("Hi {0}, what was the name of the month you were born in?".format(name))
year= input("And what year were you born in, {0}?".format(name))
day= input("And the day?")
if tmonth==month and todaydate==day:
    print ("Happy birthday!")
elif month=="October" and day=="31":
    print ("You were born on Halloween!")
    break
elif month== "December" or month== "January"  or month== "February":
    season="winter"
elif month== "March" or month== "April" or month== "May":
    season="spring"
elif month== "June" or month== "July" or month== "August":
    season="summer"
elif month== "September" or month== "October" or month== "November":
    season="fall"
else:
    print ("I don't quite understand what you said")
if year== "1980" or year== "1981" or year== "1982" or year== "1983" or year== "1984" or year== "1985" or year== "1986" or year== "1987" or year== "1988" or year== "1989":
    timeperiod="eighties"
elif year== "1990" or year== "1991" or year== "1992" or year== "1993" or year== "1994" or year== "1995" or year== "1996" or year== "1997" or year== "1998" or year== "1999":
    timeperiod="nineties"
elif year== "2000" or year== "2001" or year== "2002" or year== "2003" or year== "2004" or year== "2005" or year== "2006" or year== "2007" or year== "2008" or year== "2009" or year== "2010" or year== "2011" or year== "2012" or year== "2013" or year== "2014" or year== "2015":
    timeperiod="two thousands"
else:
    timeperiod="stone age"
print (str(name) + ", you are a " + str(season) + " baby of the " + timeperiod)