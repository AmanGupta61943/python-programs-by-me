#for loop
#range function
"""for x in range(10):
    print("hello")


#range(stop)it will run from 0-stop-1

for x in range(10):
    print(x)


#range(start,stop),it will run from start to stop-1
for x in range(1,11):
    print(x)


#range(start,stop,step), it will run from start to stop-1
for x in range(1,31,2):
    print(x)


#with increase of step
str1=input("enter a string")
for x in str1:
    print(x)


list("red","black","pink","yellow")
for x in list:
    print(x)"""




#write a program to input a string and count the number of vovel in the string

"""count=0
str2=input("enter ")
for x in str2:
    if str2 in("a","e","i","o","U"):
        count=count+1
print("number of vowels are",count)"""




#write a program to creat a list of colour with 5 colour and print the lenght of each colour along with name of colour
count=0
"""a=("red","green","yellow","pink","black")
for x in a:
    print(x,len(x))"""





#write a program to input 2 integer (a,b)and count the number of int which are muliple of 5 &3 from a to b using for loop
"""count=0
a,b=eval(input("enter"))
for x in range(a,b+1):
    if x%3==0 and x%5==0:
        print(x)
        count=count+1
print("count is", count)"""


#write a program to creat a list of 5 no. and calculate the factorial of each  no. by using for loop
"""from dataclasses import replace
import math
from xml.dom import WrongDocumentErr
a=(5,4,3,6,7)
for x in a:
    b=math.factorial(x)
    print(b)"""




#write a program to take input of 2 no. a and b and count the no. of even and odd seperatly from a to b    
"""count1=0
count2=0
a=eval(input("enter number"))
b=eval(input("enter 2nd number"))
for x in range(a,b):
    if x %2 ==0:
        count1=count1+1
    elif x%2!=0:
        count2=count2+1
print(count1)
print(count2)"""                                                         




#write a program to creat a list of 5 str and print those string from that list whose length is odd

"""str1=["hii","hlw","four","hell","five"]
for x in str1:
    if len(x)%2!=0:
        print(x)"""



#write a program to input a str and replace all the vovel with^


"""a=input("enter")
for x in a:
    if x in["a","e","i","o","U"]:
        x="*"
    print(x,end=" ")"""


#nosted for loop
"""for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()"""



"""for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()"""



"""for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()"""


"""for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()"""


for i in range(1,6):
    for j in range(1,6):
        print((i*j),end=" ")
    print()