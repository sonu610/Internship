# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 13:52:28 2020

@author: spj20
"""

l=[1,"hell",True,[3,"heaven"]]
l1=[["a","b","c"],["d","e","f"],["g","h","i"]]

racer = ["Mario", "Bowser", "Luigi"]
c=[]
len2=len(c)
print(len2)
party_attendees = ['a','b','c','d','e','f','h']
len1=len(racer)
def select_second(l):
   if len(l)>2:
       return l[1]
   else:
       return l
   
    
def purple_shell(r):
    
    
    temp=r[0]
    r[0]=r[len1-1]
    r[len1-1]=temp
    

def fashionably_late(arrivals,name):
    len3=len(arrivals)
    print(len3)
    half=round(len3/2)
    print(half)
    inx=arrivals.index(name)
    if inx>= half and inx!=len3-1:
        print("late arrival:",name)

    else:
        print("not late",name)        
   
       
   
    

print(select_second(l)) 
print("------------")

print(l1[2][1])
print("------------")

print(purple_shell(racer))
print("------------")
"""
a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1:]

# Put your predictions in the list below. Lengths should contain 4 numbers, the
# first being the length of a, the second being the length of b and so on.
lengths = [3,2,0,1]

"""

print(fashionably_late(party_attendees,'f'))
print("------------")


