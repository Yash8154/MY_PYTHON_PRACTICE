# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 12:46:05 2022

@author: Mehta Yash
"""

# list

a="hello i am yash mehta i"
a.endswith("ta")
a.find("i")
a.count("i")
b=a.replace("am","will")

c=[2,34,56,231,768,34,67,45,34]

c.insert(2,67)

c.replace(34,17) 

while(34 in c):
    c.remove(34)

x=(99,80,45,23)

x=3
y=6
x,y=y,x
print(x,y)

my_dict={"set":"contain only unique words/number",
         "mutable":"you can anytime",
         "tuple":"u cant append",
         "yash":"must be become an enterpreneur"
         }

print("""u can find meaning of only this
word which is shown in list \n""",my_dict.keys())
x=input("enter the word which you want to know meaning:")
print("The meaning of the word is..",my_dict.get(x))

x=set()

x=int(input("enter your age:"))

    
if (x in range(7,101) and x>18):
    print("you can drive a vehicle")
elif(x in range(7,101) and x==18):
    print("please come to office for test.")
else:
    print("sorry..you are not able to drive")

# 45*3=789,67+4=23,54/2=22
a=input("enter your name:")    
print("hello welcome to this app.."+a)
print("enter two number which you want to get result..")
x=int(input("enter first number:"))
y=int(input("enter second number:"))
a="summation(+)"
b="substraction(-)"
c="multiplication(*)"
d="division(/))"
z=input("type:")
if(x==45 and y==3 and z=='c'):
    print("your answer is...789")
elif(x==67 and y==4 and z=='a'):
    print("your answer is...23")
elif(x==54 and y==2 and z=='d'):
    print("your answer is...23")
elif(z=='a'):
    print("The summation is",x+y)
elif(z=='b'):
    print("The substraction is",x-y)
elif(z=='c'):
    print("The multiplication is",x*y)
elif(z=='d'):
    print("The division is",x/y)

l=[1,2,3,4,5,6]
for i in l:
    print(i)

a="5.09"
b=a.isnumeric()


i=0
while(i<45):
    print(i)
    i=i+1


while(True):
    c=int(input("enter the number:"))
    if(c<100):
        print(c)
    else:
        break


'''
3
'''
import random

com=random.randint(1,100)

i=1
print("You have only 5 tries..once try over game automatically close")
while(i<6):
   
    print("helllo,choose the number b/w 1 to 100..")
    user=int(input("guess the number:"))
    if(user>com):
        print("Your guessing is  higher")
        print("Your chance left is:",5-i)
        i=i+1
        continue
    elif(com>user):
        print("Your guessing is lower")
        print("Your chance left is:",5-i)
        i=i+1
        continue
    elif(com==user):
        print("Your Guess is correct")
        print("You took chances is",i)
        
        break
    
    
print("sorry you lose")
print("computer choose is",com)


def yash(a,b):
    """This is a function which gives a sum of two numbers"""
    c=a+b
    return c

print(yash.__doc__) #which gives what things happen in function and what we get as a return value

'''
TRY EXCEPT EXCEPTION HANDLIMG IN PYTHON

----->It's use for showing user understandable error message 
EX-When you try to search anything on google but your connection is 
suddenly lost then you get message as your connection is lost not getting 
error message as programming language..So thats why we use try exception handling
'''

x=input("enter one number:")
y=input("enter another  number:")
try:
    if(int(x)>int(y)):
        print("x is bigger")
    else:
           print("y is bigger")
except Exception:
    print("please enter integer from 0 to 10")           


a=open("yash.txt")
b=a.readlines()
for i in a:
    print(i,end="")

'''
4].Pattern Printing:-
      Input=integer n
      Boolean=True OR False
      
     OUTPUT:-
     if TRUE then:-
     say n=4
     *
     * *
     * * *
     * * * *
     if FALSE then:-
     * * * *
     * * *
     * *
     *      
      
'''
x=int(input("Enter how many row you want:"))
y=int(input("Type 1 or 0:"))
y=bool(y)
if y==True:
    for i in range(x):
        print((x-(x-1)+i) * '*')
else:
    for i in range(x):
        print((x-i)*'*')
    
'''
File handling in python in which i learned about some additional points
which is seek(),tell(),more
'''
# 1. tell():=which call a current position of pointer in file
a=open("yash.txt")
b=a.readline()
print(b)
print(a.tell())
c=a.readline()
print(c)
print(a.tell())
a.close()

#2. seek():=which relocate the pointer position as you want 
x=open("yash.txt")
y=x.readline()
print(y)
print(x.tell())
a=x.readline()
print(a)
print(x.tell())
x.seek(0)
print(x.readline())
x.seek(25)
print(x.readline())
x.close()

'''
5] problem:making health management system
'''

def gettime():
    import datetime
    return datetime.datetime.now()


def log():
    print("Choose your client")
    client = int(input("1. Harry \n2. Rohan \n3. Hammad"))
    con = 1
    if client == 1:
        while con == 1:
            print("What do you want to log for Harry?")
            choice = int(input("1. Diet \n2. Activity"))
            if choice == 1:
                f = open("yash.txt", "a")
                data = input("Enter what has Harry Eaten?")
                f.write(str([str(gettime())]) + "  " + data + "\n")
                f.close()

            else:
                f = open("harry exercise.txt", "a")
                data = input("How much time has Harry worked out?")
                f.write(str([str(gettime())]) + "  " + data + "\n")
                f.close()
            con = int(input("Do you want to log more for Harry? \n1. Yes \n2. No"))

    elif client == 2:
        while con == 1:
            print("What do you want to log for Rohan?")
            choice = int(input("1. Diet \n2. Activity"))
            if choice == 1:
                f = open("yash.txt", "a")
                data = input("Enter what has Rohan Eaten?")
                f.write(str([str(gettime())]) + "  " + data + "\n")
                f.close()

            else:
                f = open("rohan exercise.txt", "a")
                data = input("How much time has Rohan worked out?")
                f.write(str([str(gettime())]) + "  " + data + "\n")
                f.close()
            con = int(input("Do you want to log more for Rohan? \n1. Yes \n2. No"))

    elif client == 3:
        while con == 1:
            print("What do you want to log for Hammad?")
            choice = int(input("1. Diet \n2. Activity"))
            if choice == 1:
                f = open("hammad diet.txt", "a")
                data = input("Enter what has Hammad Eaten?")
                f.write(str([str(gettime())]) + "  " + data + "\n")
                f.close()

            else:
                f = open("yash.txt", "a")
                data = input("How much time has Hammad worked out?")
                f.write(str([str(gettime())]) + "  " + data + "\n")
                f.close()
            con = int(input("Do you want to log more for Hammad? \n1. Yes \n2. No"))


def retrieve():
    con = 1
    while con == 1:
        print("Choose your client")
        client = int(input("1. Harry \n2. Rohan \n3. Hammad"))
        if client == 1:
            print("What do you want to retrieve for Harry?")
            choice = int(input("1. Diet \n2. Activity"))
            if choice == 1:
                f = open("yash.txt", "r")
                print(f.readlines())
                f.close()

            else:
                f = open("yash.txt", "r")
                print(f.readlines())
                f.close()

        elif client == 2:
            print("What do you want to retrieve for Rohan?")
            choice = int(input("1. Diet \n2. Activity"))
            if choice == 1:
                f = open("yash.txt", "r")
                print(f.readlines())
                f.close()

            else:
                f = open("yash.txt", "r")
                print(f.readlines())
                f.close()

        elif client == 3:
            print("What do you want to retrieve for Hammad?")
            choice = int(input("1. Diet \n2. Activity"))
            if choice == 1:
                f = open("yash.txt", "r")
                print(f.readlines())
                f.close()

            else:
                f = open("yash.txt", "r")
                print(f.readlines())
                f.close()
    con = int(input("Do you want to retrieve any more details? \n1. Yes \n2. No"))


print("Welcome to Health care Management System")
ch = int(input("What do you want to do? \n1. Log \n2. Retrieve"))
if ch == 1:
    log()
elif ch == 2:
    retrieve()
else:
    print("Wrong Input. Please try again.")

'''
(*) Concept of global and local variable..
'''
a=56 # Global variable
def funct1(q):
    a=43 # Local variable
    m=2
    print(q,"hello..good afternoon")
    print(a,m)

"""
if we run a function we get a as 43 not 56 because..
a=43 is a function own value so first function prefer local variable
but if local variables not present then go for global variables and 
print
"""
a=56 # Global variable
def funct1(q):
    #a=43 # Local variable
    a=a+45
    m=2
    print(q,"hello..good afternoon")
    print(a,m)
"""
if you run above code then you get error msg..like that
'local variable 'a' referenced before assignment'
but if you want to run above code follow further process
"""
a=56 # Global variable
def funct1(q):
    #a=43 # Local variable
    global a
    a=a+45
    m=2
    print(q,"hello..good afternoon")
    print(a,m)

#output:a hello..good afternoon
#101 2




























































































































































































