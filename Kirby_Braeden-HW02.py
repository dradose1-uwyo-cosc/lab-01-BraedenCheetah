# Braeden Kirby
# UWYO COSC 1010
# 11/5/2024
# HW 03
# Lab Section 13
# Sources, people worked with, help given to: 

# Stack Overflow. (2024, November 5). "Is there an expansion on if statments that can stop code from continuing?". 
# https://stackoverflow.com/questions/33565519/python-if-not-this-and-not-that

# Geeks for Geeks. (2024, November 5). "Return statements and their functions". 
# https://www.geeksforgeeks.org/python-return-statement/

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

def january_first_day_calculator(year):
        
        y = year - 1

        return (36 + y + (y // 4) - (y // 100) + (y // 400)) % 7

# I can now create a validity 'checker' and make sure the entered month, day, and year are all valid and will not bring up an error

def valid_date(month, day, year):

        if month < 1 or month > 12:

                return False
        if day < 1 or day > 31:

                return False
        if year < 1:

                return False
        
# Within the validity 'checker' I can then create a dictionary to create and store the data for the days in each month

        days_in_month = {
                1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }

# I can then change february (aka 2) for if it is a leap year and the statement is True

        if it_is_leap_year(year):

                days_in_month[2] = 29

# I can set a return value to access the dictionary's original values if the if statement is not true

        return day <= days_in_month[month]

# I can now set a function to calculate the day of the week for the date given by the user

# I will staet by getting the first day of January for the given year

def day_of_week_calculator(month, day, year):

        first_day_of_january = january_first_day_calculator(year)

# I can use the month's recorded days  and then add an if statment for a leap year

        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if it_is_leap_year(year):

                days_in_month[2] = 29

# I can make the function calculate the days from january 1st through the use of how many days there are in the given month 
# then subtracting one from that day

        total_days_from_jan_1st = sum(days_in_month[:month]) + (day - 1)

        day_of_the_week = (first_day_of_january + total_days_from_jan_1st) % 7

        return day_of_the_week

# I can finally create the bulk of the program's running part by starting with defining the days of the week starting with Sunday

# I can write an input function that strips the parentheses from the dates input so that the program can actually interpret it

def main():

        days_of_the_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

        input_date = input("Please enter a date in this format (MM/DD/YYYY): ").strip()

# I can create an if statement to check that the input values have two '//' and also three parts

        parts = input_date.split('/')

        if len(parts) != 3:

                print(f"{input_date} - Invalid Date. Please try again.")

                return
        
# I can make an if not statement to check if the input values are numbers

# This was given in an example of how to check if an input value is numeric or not for what function to use

        if not (parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit()):

                print(f"{input_date} - Invalid Date. Please try again.")

                return

# I can change the parts into integers for the given month, day, and year

        month = int(parts[0])

        day = int(parts[1])

        year = int(parts[2])

# I can then try and validate the date through an if not statment 

        if not valid_date(month, day, year):

                print(f"{input_date} - Invalid Date.")

                return

        day_of_the_week_index = day_of_week_calculator(month, day, year)

        day_of_the_week_name = days_of_the_week[day_of_the_week_index]

        print(f"{input_date} - {day_of_the_week_name}")

# I can then run the program by an if statement and having the 'main()' run

if __name__ == "__main__":

        main()

# I tried using basic functions without 'def' but I wasn't able to use the 'return' statements and it made it easier to break up the program