# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 15:55:07 2022

@author: Mehta Yash
"""

'''
write a program to store seven fruits in a 
list entered by the users
'''
x=input("enter fruit n0..1:")
y=input("enter fruit n0..2:")
z=input("enter fruit n0..3:")
a=input("enter fruit n0..4:")
b=input("enter fruit n0..5:")
c=input("enter fruit n0..6:")
d=input("enter fruit n0..7:")
fruit_list=[x,y,z,a,b,c,d]
print(fruit_list)

'''
write a program to accept marks of 6 students
and display them in sorted manner

'''
x=input("enter the students marks:")
y=input("enter the students marks:")
z=input("enter the students marks:")
a=input("enter the students marks:")
b=input("enter the students marks:")
c=input("enter the students marks:")
marks=[x,y,z,a,b,c]
print(marks)
marks.sort()
print(marks)

'''
check that the tuple cant be changed in pyhton

'''
y=(6,7,8)
print(y)
y[1]=98
print(y)

'''
write a program to sum a list with 4 numbers

'''
x=int(input("enter the number:"))
y=int(input("enter the number:"))
z=int(input("enter the number:"))
a=int(input("enter the number:"))
l1=[x,y,z,a]
print("the sum of four number is:",l1[0]+l1[1]+l1[2]+l1[3])
print("the sum of four number is...",sum(l1))

'''

write a program to count number of zero 
in following tuple

'''
a=(7,0,8,0,0,9)
print("the no. of zero in tuple is...",a.count(0))






















































