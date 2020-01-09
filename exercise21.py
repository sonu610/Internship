# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 13:24:37 2020

@author: spj20
"""

def onionless(ketchup, mustard, onion):
    """Return whether the customer doesn't want onions.
    """
    return not onion

def ketchupless(ketchup, mustard, onion):
    """Return whether the customer doesn't want onions.
    """
    return not ketchup

def mustardless(ketchup, mustard, onion):
    """Return whether the customer doesn't want onions.
    """
    return not mustard

def wants_all_toppings(ketchup, mustard, onion):
    return ketchup and mustard and onion

def wants_plain_hotdog(ketchup, mustard, onion):
      return not(ketchup and mustard and onion)
  
def exactly_one_sauce(ketchup, mustard, onion):
    if ketchup:
        return ketchup and onion
    else:
        return mustard and onion
    
    
    #return (ketchup and not mustard) or (mustard and not ketchup)
    
def exactly_one_topping(ketchup, mustard, onion):
    if int(ketchup)==1:
        return ketchup
    elif int(mustard)==1:
        return mustard
    else:
        return onion
    
onion=True
ketchup=True
mustard=True
print("i want mustardless burger so mustard=",mustardless(ketchup,mustard,onion))