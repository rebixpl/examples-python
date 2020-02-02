import calendar

# it prints all days of week in a row you can put a number (here 3) which
# describes the length (3 letters) of each day name
print(calendar.weekheader(3))
print()

# prints out the first day of the week which is MONDAY (index: 0 )
print(calendar.firstweekday())
print()

# prints out entire month (the first argument is year and the second one is a month which we want to print out)
# w = The width between two columns
# l = Blank line between two rows
print(calendar.month(2019, 12, w=3, l=2))
print()

# it makes a LIST of days in selected month
print(calendar.monthcalendar(2019,12))
print()

# it prints whole YEAR calendar
print(calendar.calendar(2019))
print()

# it prints out the index of day you need to give (year, month, day), in this case it would be 2 which corresponds with Wednesday
day_of_the_week = calendar.weekday(2019, 12, 25)
print(day_of_the_week)
print()

#it checks if the year is leap (przestępny)
is_leap = calendar.isleap(2019)
print(is_leap)
print()

#it tells you how many leap days are in the range of years
how_many_leap_days = calendar.leapdays(2000, 2050)
print(how_many_leap_days)
print()
