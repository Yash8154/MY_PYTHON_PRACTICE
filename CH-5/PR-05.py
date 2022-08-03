# -*- coding: utf-8 -*-
'''
write a program to create a dictionary of hindi words
with values as their english transformation
provide user with an option to look it up

'''
mydict={
        "chamch":"spoon",
        "thali":"dish",
        "katori":"bowl"
        }
print("options are:",list(mydict.keys()))
while(True):
    x=input("enter the hindi word:").lower()
    if(x=="done"):
            break
#  print("english meaning is:",mydict[x])
    print("english meaning is:",mydict.get(x))
   
'''
write a program to input eight numbers from the 
user and display all the unique numbers(once).

'''
x=input("enter the no.")    
y=input("enter the no.")    
z=input("enter the no.")    
a=input("enter the no.")    
b=input("enter the no.")    
c=input("enter the no.")    
d=input("enter the no.")    
e=input("enter the no.")
h=set()
h.add(x)    
h.add(y)    
h.add(z)    
h.add(a)    
h.add(b)    
h.add(c)    
h.add(d)    
h.add(e) 
print(h) 

'''
can we have a set with 18(int) and "18"(str)
as a values in it ?

'''
a=set()
b=int(input("enter the number:"))
c=input("enter the number")
a.add(b)
a.add(c)
print(a)
#yes..set have both string and integer...

'''
create an empty dictionary,allow 4 friends to enter
their favourite language as values and use keys as 
their names.Assume that the names are unique

'''
d={}
x=input("enter the language name:")
y=input("enter the language name:")
z=input("enter the language name:")
update_dict={
 "yash":x,
"harsh":y,
"parth":z   
    }
d.update(update_dict)
print(d)


    
    
    
    
    
    
    
    
    
    
    
    
    
    