# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 12:57:53 2020

@author: spj20
"""

def sign(n):
    if n>0:
        return 1
    elif n<0:
        return -1
    else:
        return 0

def to_smash(total_candies):
    if total_candies == 1:
        print("Splitting 1 candy")
    else:
        print("Splitting", total_candies, "candies")
    
        print("divided candies:",total_candies//3)
    return total_candies % 3
def concise_is_negative(number):
    return True if number<0 else False

def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    # Don't change this code. Our goal is just to find the bug, not fix it!
    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

# Change the values of these inputs so they represent a case where prepared_for_weather
# returns the wrong answer.
have_umbrella = False
rain_level = 0.0
have_hood = True
is_workday = True

# Check what the function returns given the current values of the variables above
actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual)
print("---")
print(to_smash(91))
print(to_smash(1))
print("---")
print(sign(18))
print(sign(-18))
print("---")
print(concise_is_negative(100))
    