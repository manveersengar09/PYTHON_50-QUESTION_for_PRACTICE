
"""
QUES 11}.py
•   Check for Leap Year
•	Write a function to check if a given year is a leap year.
•	A leap year is divisible by 4, but not by 100, unless also divisible by 400.
•	Divisible by 4: If a year can be evenly divided by 4 (like 2020), it might be a leap year.
•	Not Divisible by 100: However, if that year can also be evenly divided by 100 (like 1900), then it's not a leap year.
•	Unless Divisible by 400: If the year is divisible by 100, it could still be a leap year if it can also be evenly divided by 400 (like 2000).

•	Example
Input: year = 2020
Expected Output: True (2020 is a leap year)
•	Example
Input: year = 1900
Expected Output: False (1900 is not a leap year)
•	Example
Input: year = 2000
Expected Output: True (2000 is a leap year)
"""
def is_leap_year(year):
    """
    Returns True if the given year is a leap year, False otherwise.
    """
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
    

# Examples:
print(is_leap_year(2020))  # Output: True
print(is_leap_year(1900))  # Output: False
print(is_leap_year(2000))  # Output: True
