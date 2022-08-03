# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 16:53:38 2022

@author: Mehta Yash
"""

'''
1.
'''

def x(a,b,c):
    if(a>b>c):
        return(a,"bigger")
    elif(b>a>c):
        return(b,"bigger")
    elif(c>b>a):
        return(c,"bigger")

'''
2
'''

a=9
b=5
c=32
def fahrenheit(x):
    return((a*x)/b)+c

'''
3
'''
print("hello yash...",end=" ")
print("oh i m fine..what about you")
    
'''
4
'''
def sum(n):
    if n==0:
        return 0
    return n + sum(n-1)
    
a=100
b=sum(a)
print("the sum of first",+a,"number is-->",+b) 

'''
5
'''
n=3
for i in range(n):
    print("*" * (n-i))


'''
6
'''
def centi(x):
    return 2.54*x
a=3
b=centi(a)
print("the conversion in ceti is..",b)

'''
7
'''

def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "    yash is a good      "
n = remove_and_split(this, "yash")
print(n)    
 
'''
8
'''
def multiplication(x):
    for i in range(1,11):
         print(x*i)

        
    
 
    
 
    
 
    
 
    
 
    
 
    
    