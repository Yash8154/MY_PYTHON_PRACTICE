# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 18:41:54 2022

@author: Mehta Yash
"""

'''
write a program to print table of any number given
by users
'''
x=int(input("enter the number:"))
i=1
while(i<=10):
    print(x*i)
    i=i+1
x=int(input("enter the number:"))

for i in range(1,11):
    print(x*i)
    

'''
write a program to greet all the person names starts with
S stored in list l1
l1=["yash","soham","sachin","rahul"]

'''
l1=["yash","soham","sachin","rahul"]
for i in l1:
    if(i.startswith("s")):
        print("Hello",i)

'''
write a program to find wheather a given number is 
prime or not.
'''
x=int(input("enter the number:"))
for i in range(2,x):
    if(x%i==0):
        print("number is not prime")
        break
else:
        print("number is prime ")
        
'''
write a python program to find sum of first n 
natural number using while loops

'''
x=int(input("enter the no you want to add:"))
i=1
while(i<=x):
    a=(i*(i+1)/2)
    i=i+1
    
print(a)

'''
6
'''

num = int(input("Enter the number: "))
factorial = 1
for i in range(1, num+1):
    factorial = factorial * i
print(f"The factorial of {num} is {factorial}")





x=int(input("enter the num:"))
y=(x*(x+1))/2
print(y)


m=5
for i in range(0,5):
    print("*"*(i+1))


n = 3
for i in range(3): 
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))
n=3
print("*"+"*"*(n-0-1))
a=print("*"+" "+"*"*(n-0-2))
print("*"+"*"*(n-0-1))



x=int(input("enter the number:"))
for i in range(1,11):
    print(x*(11-i))



n=3
for i in range(0,3):
    print("*",end="")
    if((n*i)-n==0):
        print(" ",end="")
    else:
        print("*",end="")
    print("*")
   
   













