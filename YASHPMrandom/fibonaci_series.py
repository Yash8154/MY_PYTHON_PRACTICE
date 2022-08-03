# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 16:38:35 2022

@author: Mehta Yash
"""

'''
Fibonaci series
'''
x=int(input("enter the number:"))
a=1
b=1
c=a+b
list1=[]
list1.append(a)
list1.append(b)
list1.append(c)
for i in range(1,x+1):
    
        y=list1[i]+list1[i+1]
        list1.append(y)
print(list1)

#  1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,......
