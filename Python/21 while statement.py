"""i=1
while i<=10:
    print("hello")
    i=i+1"""

#write aprogram to print 1 to 10 number using while loop

"""i=1
while i<=10:
    print(i)
    i=i+1"""

#write a program to input a number and print a multipication table of that number upto 10 in th following formate


"""x=eval(input("enter a number"))
y=1
while y<=10:
    print("{}*{}={}".format(x,y,x*y))
    y=y+1"""


#write a program to print factorial of a number using y loop

from re import I


"""n=eval(input("enter a number"))
i=1
f=1
while i<n:
    f=f*i
    i=i+1
print("factorial is",f)"""


#write a program to inputa a number to print all the number from 1 to n which are divisible by 3 as well as 5

"""n=eval(input("enter a number"))
i=1
while i<=n:
    if i%3==0 and i%5==0:
        print(i)
    i=i+1"""


#write a program to print reverser of a number by using y loop

n=eval(input("enter a number"))
rev=0
while n!=0:
    t=n%10
    rev=rev*10+t
    n=n//10
print("reverse is",rev)