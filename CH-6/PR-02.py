# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 16:16:31 2022

@author: Mehta Yash
"""

'''
write a python program to find wheather a given username contain 10
character or not.
'''
x=input("enter any word:")
if(len(x)>=10):
    print("word length is atleast 10 character..the length is",len(x))
else:
    print("word length is less than 10 character..the length is",len(x))