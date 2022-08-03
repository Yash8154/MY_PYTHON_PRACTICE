# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 16:04:35 2022

@author: Mehta Yash
"""

print("Hello,welcome to this amazing game..")
print("""In this game computer select random word from 
the list..list contain top 10 indian companies name""")
print("""you give the number of word and according that
you select the word one by one""")
print("Remeber you have only 10 tries..")
print("Let's start this game")
list1=["boat",'tata','birla','reliance','paytm','flipkart','myntra','snapdeal','paris','lifeline']
import random
computer=random.choice(list1)
a='abcdefghijklmnopqrstuvwxyz'
print("selected word has a letter is..",len(computer))
list2=[]
for i in computer:
      list2.append('_')
print(list2)
tries=0
while(tries<=10):
    x=input("enter the word:")
    if x not in a:
        print("try again...")
    if x in computer:
        print("your guess word is match")
        for j in range(0,len(computer)):
            if(computer[j]==x):
                list2[j]=x
        print(list2)
  
        if('_' not in list2):
             print("player win")
             break
    else:
         print("your pick is incorrect")
         tries+=1
else:
    print("player loose and selected word is",computer)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    