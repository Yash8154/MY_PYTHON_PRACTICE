# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 14:47:08 2022

@author: Mehta Yash
"""

'''
1
'''
f=open("twinkle.txt",'r')
a=f.readline()
b=a.split()
print(b)
for i in range(0,10):
    if(b[i]=='twinkle'):
        print("yes the word is present")
        break
    else:
        print("sorry...word is not present")
f.close()


'''
2
'''
def game():
    return 56
score=game()
with open("hiscore.txt") as f:
    hiscore=int(f.read())
if hiscore<score:
    with open("hiscore.txt",'w') as f:
        f.write(str(score))
'''
4
'''
with open("donkey.txt") as f:
    a=f.read()
    x=a.replace("donkey","######")
    with open("donkey.txt",'w') as f:
        y=f.write(x)
'''
5
'''
list1=['better']
with open("donkey.txt") as f:
    a=f.read()
for i in list1:
    
    x=a.replace(i,"######")
    with open("donkey.txt",'w') as f:
        y=f.write(x)
'''
6
'''
with open("log.txt") as f:
    a=f.read().lower()
if "python" in a:
    print("yes")
else:
    print("no")
    
'''
7
'''
content = True
i = 1
with open("log.txt") as f:
    while content:
        content = f.readline()
        if 'python' in content.lower():
            print(content)
            print(f"Yes python is present on line number {i}") 
        i+=1    
'''
8
'''
with open("helo.txt") as f:
    a=f.read()
    with open("copy.txt",'w') as f:
        b=f.write(a)
'''
9
'''
file1 = "log.txt"
file2 = "copy.txt"

with open(file1) as f:
    f1 = f.read()

with open(file2) as f:
    f2= f.read()

if f1 == f2:
    print("Files are identical")
else:
    print("Files are not identical")
    
'''
10
'''
with open("hiscore.txt",'w') as f:
    a=f.write("")
   
'''
11
'''
import os
x="E:\\PYTHON PRACTICE\\CH-09\\renamed_by_python.txt"
y="E:\\PYTHON PRACTICE\\CH-09\\copy.txt"
os.rename(x,y)

#.....................
import os
old_name="yash.txt"
new_name="renamed_by_python.txt"
with open(old_name) as f:
    a=f.read()
    with open(new_name,'w') as f:
        b=f.write(a)
        
os.remove(old_name)
    


























































































































