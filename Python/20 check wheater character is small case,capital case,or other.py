#write a program to enter a character and check wheater character is small case,capital case,or other
"""ch=(input("enter a character"))
if ch>="a" and ch<="z":
    print(ch,"is a small letter")
elif ch>="A" and ch<="Z":
    print(ch,"is a capital letter")
else:
    print(ch,"is other then a letters")"""

#write a program to input the percentage obtain from a user to 


"""a=eval(input("enter percentages"))
if a>90:
    print(a,"is A grade")
elif a>80 and a<=90:
    print(a,"is B grade")
elif a>=60 and a<=80:
    print(a,"is C grade")
else:
    print(a,"is D grade")"""


#write a program to accept to accept a number 

"""cost=eval(input("enter the cost of bike"))
if cost>100000:
    t=cost*.15
    print("road tax is",t)
elif cost>50000 and cost<=10000:
    t=cost*0.1
    print("road tax is",t)
elif cost<=50000:
    t=cost*0.05
    print("road tax is",t)"""


#
"""sal=eval(input("enter the salary"))
yrs=eval(input("enter the number of year"))
if yrs>10:
    b=sal*0.15
    print("bonus is",b)
elif yrs>=6 and yrs<=10:
    b=sal*0.10
    print("bonus is",b)
else:
    b=sal*0.05
    print("bonus is",b)"""


#writ a program to input 2 variable a,b and take input of opration to be performed if user input +=a+b,-=a-b,*=a*b,a//b

"""a,b=eval(input("enter"))
op=input("perform")
if op=="+":
    print("addition is",a+b)
elif op=="-":
    print("sub is",a-b)
elif op=="*":
    print("mul is",a*b)
elif op=="//":
    print("div is",a//b)
else:
    print("invalid operation")"""





#write a progeam to check whethe a year is said to leap year 
"""yr=eval(input("enter year to check"))
if yr%100==0:
    if yr%400==0:
        print(yr,"is leap year")
    else:
        print(yr,"is not a leap year")
elif yr%4==0:
    print(yr,"is a leap year")
else:
    print(yr,"is not a leap year")"""


#
u=eval(input("enter units consumed"))
if u<=100:
    print("free electricity")
elif u>100 and u<=300:
    b1=(u-100)*2
else:
    b2=(u-300)*5+400
    print("total bill is",b2)