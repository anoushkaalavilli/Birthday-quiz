"""
birthday.py
Author: Anoushka Alavilli
Credit: <list sources used, if any>
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
todaydate = datetime.today().day
tmonth= str(todaymonth)
tday= str(todaydate)
name= input("Hello, what is your name?")
month= input("Hi {0}, what was the name of the month you were born in?".format(name))
year= input("And what year were you born in, {0}?".format(name))
day= input("And the day?")
if month== "december" or "December" or "january" or "January" or "february" or "February":
    season="winter"
elif month== "March" or "march" or "April" or "april" or "May" or "may":
    season="spring"
elif month== "June" or "june" or "July" or "july" or "August" or "august":
    season="summer"
elif month== "September" or "september" or "October" or "october" or "November" or "november":
    season="fall"
else:
    print ("I don't quite understand what you said")
if tmonth==month and tday==day:
    print ("Happy birthday!")
elif month=="October" or "october" and day=="31":
    print ("You were born on Halloween!")
elif year=="1980" or "1981" or "1982" or "1983" or "1984" or "1985" or "1986" or "1987" or "1988" or "1989":
    timeperiod="eighties"
elif year== "1990" or "1991" or "1992" or "1993" or "1994" or "1995" or "1996" or "1997" or "1998" or "1999":
    timperiod="nineties"
elif year== "2000" or "2001" or "2002" or "2003" or "2004" or "2005" or "2006" or "2007" or "2008" or "2009" or "2010" or "2011" or "2012" or "2013" or "2014" or "2015":
    timperiod="two thousands"
else:
    timeperiod="stone age"







print ("{0}, you are a {1} baby of the {2}".format(name, season, timeperiod))