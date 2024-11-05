# Braeden Kirby
# UWYO COSC 1010
# 11/5/2024
# HW 03
# Lab Section 13
# Sources, people worked with, help given to: 

# Assignment Information:

# Your goal for this program is to write a program that given a date of the format MM/DD/YYYY, your program will then
# state the day of the week the date occurs on.
# Given Notes:

# April, June, September, November have 30 days

# January, March, May, July, August, October, December have 31 days

# February typically has 28 days, 29 in a leap year

# Leap years occur in years equally divisible by 4, and not by 100 except in the case when they are
# divisible by 400. So 2000 was a leap year, however 2100 will not be

# Assume that Sunday is day 0 with Saturday being day 6

# The day of the week that January 1st falls on can be determined using the following equation:

# let y = year -1
# Jan first falls on day x where:
# day = (36 + y +(y/4) - (y/100) + (y/400))%7

# This equation uses integer division rounded down

# Once this is found, you can find what day of the week all other dates fall on. Your program should check for
# invalid input. Make sure you are checking if it is a leap year if 2/29/XXXX is entered for example, and that
# none of the other dates are going out of bounds. If the input is not valid, the dates supplied don’t work, etc
# alert the user to the issue.

# Input

# Your code should accept input from the command line. Dates in the form of MM/DD/YYYY will be inputted.

# Output

# Your code should output the inputted date followed by the day of the week it falls on, or that is invalid:

# 02/21/2022 Monday

# 01/01/2022 Saturday

# 02/29/2024 Thursday

# 02/29/2023 Invalid Date

# 04/31/2023 Invalid Date

# 02/00/2023 Invalid Date

# Hints

# Here are some suggestions, they aren't required but they will make your life easier:

# Break things down into functions, such as:
# Checking if it is a leap year
# Calculating on what day January 1st occurs
# Checking if the date entered is valid
# Calculating the day of the week for the supplied date
# Utilize data structures!
# This helps make your code more concise
# And also is easier to program
# A dictionary to map months with their days
# A list for days of the week
# etc
# // is Python's floor division
# Meaning, it will divide two numbers and give you the integer result rounded down
# 9//2 would give 4 for example
# Have a calendar open when testing this
# Test edge cases
# leap days in leap years and not
# Days after a leap day
# Going out of bounds in a month
# etc

# DISALLOWED

# You CANNOT use external libraries to determine the day of the week something occurs on, 
# e.g the DateTime library. Doing so will result in your program receiving a 0. You must write all the solution yourself.

# I can start by defining a function to check if the year is a leap year using if and else's to set the function (if it is a leap year) to be True or False

def it_is_leap_year(year):
        
        if year % 4 == 0:

                if year % 100 == 0:

                        if year % 400 == 0:
                                
                                return True
                        
                        else:

                                return False
                
                return True
        
        return False       

# I can then go to the next helpful hints step and make a fucntion to find out what day January 1st is for each year

def first_january_day_calculator(year):
        
        y = year - 1 



