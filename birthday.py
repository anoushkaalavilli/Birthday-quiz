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
name= input("Hello, what is your name?")
month= input("Hi {0}, what was the name of the month you were born in?".format(name))
year= input("And what year were you born in, {0}?".format(name))
day= input("And the day?")
if month is "december" or "December" or "january" or "January" or "february" or "February":
    season="winter"
elif month is "March" or "march" or "April" or "april" or "May" or "may":
    season="spring"
elif month is "June" or "june" or "July" or "july" or "August" or "august":
    season="summer"
elif month is "September" or "september" or "October" or "october" or "November" or "november":
    season="fall"
else:
    print ("I don't quite understand what you said")
if year is "1980" or "1981" or "1982" or "1983" or "1984" or "1985" or "1986" or "1987" or "1988" or "1989":
    timeperiod="eighties"
elif int(year) is i in range (1990, 1999):
    timperiod="nineties"







print ("{0}, you are a...".format(name))