# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 15:55:01 2020

@author: spj20
"""

def is_valid_zip(zip_code):
  l1=len(zip_code)
  if l1==5:
        if zip_code.isdigit():
            return True
  
  return False 

documents=["hello world","this is not a cat","i hate your world"]
keyword="world"
keywords=["world","not"]


def word_search(documents, keyword):
   
    index = [] 
    for i, doc in enumerate(documents):
       
        tokens = doc.split()
        print(tokens)
       
      
        if keyword.lower() in tokens:
            index.append(i)
    return index
    
print(word_search(documents, keyword))

def multi_word_search(documents, keywords):
    dic= {}
    for keyword in keywords:
        dic[keyword] = word_search(documents, keyword)
    return dic


print(multi_word_search(documents, keywords))
