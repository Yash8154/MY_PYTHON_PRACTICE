# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 18:24:00 2022

@author: Mehta Yash
"""

'''
Snake vs. Water: Snake drinks the water hence wins.
Water vs. Gun: The gun will drown in water, hence a point for water
Gun vs. Snake: Gun will kill the snake and win.

In situations where both players choose the same object, the result will be a draw.
'''
import random
x=["water","snake","gun"]
computer_guess=random.choice(x)
p=0
c=0
while(True):
    for i in range(1,6):
        print("round",i,"start")
        player=input("choose the word:").lower()
        computer_guess=random.choice(x)

        print("computer choose is...",computer_guess)
        if(player=="snake" and computer_guess=="water"):
            print("player win this round")
            p+=1
        elif(player=="water" and computer_guess=="gun"):
             print("player win this round")
             p+=1
        elif(player=="gun" and computer_guess=="snake"):
            print("player win this round")
            p+=1
        elif(player==computer_guess):
            print("Draw this round")
            p+=1
            c+=1
        else:
            print("computer win this round")
            c+=1
    
    if(p>c):
        print("player win this game")
        print("your score",p,"computer score",c)
    elif(c>p):
        print("computer win this game")
        print("your score",p,"computer score",c)
        
    else:
        print("draw this game")
        print("your score",p,"computer score",c)
    print("are you interested to play again ?")
    user=input("enter the response--->")
    if(user=='yes' or user=='YES' or user=='Yes'):
        continue
    elif(user=='no' or user=='NO' or user=='No'):
        break
    
       
      
    
        
        
        
        
        
        
        
        
        
        
        
        