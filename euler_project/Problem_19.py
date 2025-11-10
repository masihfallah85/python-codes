#Problem_19

"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

def leap_year(year):

    """This function returns if a year is leap year or not"""

    return (year % 4 == 0 and year % 100  != 0) or (year % 100 == 0  and year % 400 == 0)

#Create a variable to count first of month sundays
sunday = 0

#Create variable for first day of month by day of week,assume indexing starts with saturday as 0 and friday as 6,and 1 jan 1901 is tuesday
day = 3

#iterate through years to count,assume indexing starts with saturday as 0 and friday as 6
for i in range(1901,2001):

    for j in range(1,13):

        if j in [1,3,5,7,8,10,12]:

            day = (day + 31) % 7

            sunday = sunday + 1 if day == 1 else sunday

        elif j in[4,6,9,11]:

            day = (day + 30) % 7

            sunday = sunday + 1 if day == 1 else sunday

        elif j == 2 and leap_year(i):

            day = (day + 29) % 7

            sunday = sunday + 1 if day == 1 else sunday

        else:

            day = (day + 28) % 7

            sunday = sunday + 1 if day == 1 else sunday

#Print the result
print(f"{sunday}  sundays are first of the month")
