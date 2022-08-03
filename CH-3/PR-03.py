# -*- coding: utf-8 -*-
"""
Created on Sat May 28 16:12:39 2022

@author: Mehta Yash
"""
"""
write a program to display a user entered name followed 
by Good Afternoon using input function

"""

x=input("Enter your name:")
y="  Good Afternon "
print(x+y)

"""
write a program to fill in a letter template given 
below with name and date
"""
letter=""" Dear <Name>
            you are selected!
            <Date>"""
            
letter=letter.replace("<Name>","Yash P Mehta")
letter=letter.replace("<Date>","17/09/2022")
print(letter)

"""
write a program to detect double spaces in  string
"""
x="hi i m  yash mehta  from home"
x.find("  ")

"""
write a program to replace double spaces by single 
space in  string
"""
x="hi i m  yash mehta  from home"
y=x.replace("  "," ")
print(y)

"""
write a program to format the following
letter using escape sequence chracters

"""
x="Hello,Dear Yash mehta,Thanks for attend our function"
print(x)
formated_x="Hello,\n\tDear Yash mehta,\n\t\tThanks for attend our function"
print(formated_x)






























