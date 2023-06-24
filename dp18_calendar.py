# Get year from user
# Get month from user
# Print Calendar of that month, Year


"""
!START
? ---------- Input -------------
Year: 2017
Month: 04
? ---------- Output -------------
     April 2017                             
Mo Tu We Th Fr Sa Su                 
                1  2                                
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30

!END
"""

"""
? -------------> Pseudocode
=> Import the calendar library
=> Get year and month in yr and mn variable
=> Use calendar.month function to get the required calendar
=> Print the calendar
"""

import calendar


def main():
    yr = int(input("What's Year? "))
    mn = int(input("What's Month? "))
    print(calendar.month(yr, mn))


if __name__ == "__main__":
    main()
