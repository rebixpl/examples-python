#! /usr/bin/python3

###! Python Datetime

##? Python dates
#       * we need to mport 'datetime' to work with dates as date objects
import datetime

x = datetime.datetime.now()
print(x) # OUTPUT: 2020-01-21 16:18:03.978426

print(x.year) # OUTPUT: 2020

print(x.strftime("%A")) # OUTPUT: Tuesday



##? Creating Date Objects
import datetime

z = datetime.datetime(2020,4,13)

print(z)
print("")



##? The strftime() method
#       * The datetime object has a method for formatting date objects into readable strings.
#       * The method is called strftime(), and takes one parameter, format, to specify the format of the returned string.
import datetime
c = datetime.datetime(2018,6,1)
print(c.strftime("%B"))
print("")

#! %a -> Weekday, short version -> Wed
print(c.strftime("%a")) # OUTPUT:Fri

#! %A -> Weekday, full version -> Wednesday
print(c.strftime("%A")) # OUTPUT:Friday

#! %w -> Weekday as a number 0-6, 0 is a Sunday -> 3
print(c.strftime("%w")) # OUTPUT:5

#! %d -> Day of month 01-31 -> 31 
print(c.strftime("%d")) # OUTPUT:01

#! %b -> Month name, short version -> Dec
print(c.strftime("%b")) # OUTPUT: Jun

#! %B -> Month name, full version -> December
print(c.strftime("%B")) # OUTPUT: June

#! %m -> Month as a number 01-12 -> 12
print(c.strftime("%m")) # OUTPUT: 06

#! %y -> Year, short version, without century -> 18
print(c.strftime("%y")) # OUTPUT: 18

#! %Y -> year, full version -> 2018
print(c.strftime("%Y")) # OUTPUT: 2018

#! %H -> Hour 00-23 -> 17
print(c.strftime("%H")) # OUTPUT: 00

#! %I -> Hour 00-12 -> 05
print(c.strftime("%I")) # OUTPUT: 12

#! %p -> AM/PM -> PM
print(c.strftime("%p")) # OUTPUT: AM

#! %M -> Minute 00-59 -> 41
print(c.strftime("%M")) # OUTPUT:00

#! %S -> Second 00-59 -> 08
print(c.strftime("%S")) # OUTPUT: 00

#! %f -> Microsecond 000000-999999 -> 548531
print(c.strftime("%f")) # OUTPUT: 000000

#! %z -> UTC offset -> +0100
print(c.strftime("%z")) # OUTPUT: lack of data

#! %Z -> Timezone -> CST
print(c.strftime("%Z")) # OUTPUT: lack of data

#! %j -> Day number of year 001-366 -> 365
print(c.strftime("%j")) # OUTPUT: 152

#! %U -> Week number of year, Sunday as first day of week, 00-53 -> 52
print(c.strftime("%U")) # OUTPUT: 21

#! %W -> Week number of year, Monday as the first day of the week, 00-53 -> 52
print(c.strftime("%W")) # OUTPUT: 22

#! %c -> Local version of date and time -> Mon Dec 31 17:41:00 2018
print(c.strftime("%c")) # OUTPUT: Fri Jun 1 00:00:00 2018

#! %x -> Local version of date -> 12/31/18
print(c.strftime("%x")) # OUTPUT: 06/01/18

#! %X -> Local version of time -> 17:41:00
print(c.strftime("%X")) # OUTPUT: 00:00:00

#! %% -> A % character -> %
print(c.strftime("%%")) # OUTPUT: %
