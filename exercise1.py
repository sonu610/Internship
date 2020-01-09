# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 11:31:10 2020

@author: spj20
"""


print("hola...")
help(round)
help(round(-2.01))
help(print)

def round_to_two_places(num):
    return round(num,2)
def round_to_two_place(num):
    return round(num,-2)
def to_smash(total_candies,n=3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    return total_candies % n


print(round_to_two_places(23.23569))
print(round_to_two_places(96.12345))
print(to_smash(168,4))
print(to_smash(167))
print(round_to_two_place(23.23569))
print(round_to_two_place(96.12345))