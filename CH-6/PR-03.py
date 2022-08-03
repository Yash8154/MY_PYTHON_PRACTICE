# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 16:32:40 2022

@author: Mehta Yash
"""

'''
write a progran to calculate grade of a student...
'''
student=int(input("enter your marks:"))
if(student in range(91,101)):
    print("your grade is..excellent")
elif(student in range(81,91)):
    print("your grade is..A")
elif(student in range(71,81)):
    print("your grade is..B")
elif(student in range(61,71)):
    print("your grade is..C")
elif(student in range(51,61)):
    print("your grade is..D")
else:
    print("you are a fail")
    
