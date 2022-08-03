# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 17:04:01 2022

@author: Mehta Yash
"""

'''
1
'''
class Employee:
    company="Microsoft"
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        print("employee is created")
    def getdetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The age of the employee is {self.age}")
        print(f"The salary of the employee is {self.salary}")
            
yash=Employee("Yash",22,100)
harsh=Employee("Harsh",22,300)
monil=Employee("Monil",22,500)
yash.getdetails()
harsh.getdetails()
monil.getdetails()

'''
2 #square,cube,SR
'''
class Calculator:
    def __init__(self,number):
        self.number=number
        self.square=number * number
        self.cube=number * number * number
        import math
        self.sr=math.sqrt(number)
    def solution(self):
        print(f"The given input is {self.number}")
        print(f"The square of the num..is {self.square}")
        print(f"The cube of the num..is {self.cube}")
        print(f"The sr of the num..is {self.sr}")
num1=Calculator(4)
num1.solution()
        


'''
3
'''
class Sample:
    a = "Yash"

obj = Sample()
obj.a = "Vikky"
# Sample.a = "Vikky"

print(Sample.a)
print(obj.a)

'''
4
'''

class Calculator:
    def __init__(self,number):
        self.number=number
        self.square=number * number
        self.cube=number * number * number
        import math
        self.sr=math.sqrt(number)
        
    @staticmethod
    def grett():
        print("hello")
    def solution(self):
        print(f"The given input is {self.number}")
        print(f"The square of the num..is {self.square}")
        print(f"The cube of the num..is {self.cube}")
        print(f"The sr of the num..is {self.sr}")
  
num1=Calculator(4)
num1.grett()
num1.solution()
        

'''
5
'''
'''
1 2 3 4 5 6 7 8 9 10
'''
list1=[1,2,3,4,5]
list2=[]
class Train:
    def __init__(self, name, fare, list1,list2):
     

        self.name = name
        self.fare = fare
        self.seats = len(list1)

    def getStatus(self):
        print("************")
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")
        print("************")

    def fareInfo(self):
        print(f"The price of the ticket is: Rs {self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry this train is full! Kindly try in tatkal")

    def cancelTicket(self, seatNo):
        list2.append(seatNo)
        self.seats=self.seats+len(list2)

intercity = Train("Intercity Express: 14015", 90, list1,list2)
intercity.getStatus() 
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()
intercity.cancelTicket(5)
intercity.getStatus()

'''
6
'''
class Sample: 
    def __init__(slf, name):
        slf.name = name

obj = Sample("yash") 
print(obj.name) 
 























































