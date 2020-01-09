# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 15:12:58 2020

@author: spj20
"""
l=[1,2,3,4]
thresh=2

mealmenu=["a","a","g","f"]
def elementwise_greater_than(l, thresh):
    """Return a list with the samturne length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]"""
    
    result=[]

    for i in l:
        
        result.append(i>thresh)
    return result
  
def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    for x in range(len(meals)-1):    
    
        if meals[x]==meals[x+1]:
            return True
        else:
            return False
 
    

res=elementwise_greater_than(l, thresh)
print(res)
print("-------------")

print("2 days in row:",menu_is_boring(mealmenu))