# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 18:40:37 2022

@author: Mehta Yash
"""

"""
write a program to find greatest of four numbers entered by the users

"""
x=int(input("enter the number:"))
y=int(input("enter the number:"))
z=int(input("enter the number:"))
a=int(input("enter the number:"))
if(x>y and x>z and x>a):
    print("x is largest")
elif(y>x and y>z and y>a):
    print("y is greatest")
elif(z>y and z>x and z>a):
    print("z is greatest")
elif(a>y and a>z and a>x):
    print("a is greatest")
elif(x==y or x==z or x==a or x>y>z>a):
    print("x is greatest")
elif(y==x or y==z or y==a or y>x>z>a):
    print("y is greatest")
elif(z==y or z==x or z==a or z>y>x>a):
    print("z is greatest")
elif(a==y or a==z or a==x or a>y>z>x):
    print("x is greatest")




"""
write a program to find out wheather a student is pass
or fail,if it requires total 40% and at least 33%,in each
subject to pass.Assume 3 subjects and take marks as an
input from the users

"""
a=300
x=int(input("enter the phy. marks:"))
y=int(input("enter the chem. marks:"))
z=int(input("enter the math marks:"))
marks=[]
marks=[x,y,z]
print(marks)
if(marks[0]<33 or marks[1]<33 or marks[2]<33):
    print("you are fail in atleast one subjects")
elif(marks[0]>=33 and marks[1]>=33 and marks[2]>=33):
    print("you are pass in all subjects")
    print(" congratulations..your percentage is",((marks[0]+marks[1]+marks[2])/a)*100)  
    





































