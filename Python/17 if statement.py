"""num=eval(input("enter a number"))
if num>0:
    print("i am inside if")
    print("number is positive")
print("i am outside if")"""


#to find greater of 2 number

'''a,b=eval(input("enter the value of a anb b"))
if a>b:
    print("{} is greater".format(a))
else:
    print("{} is greater".format(b))'''

#checck whether a number is odd or even

'''num=eval(input("enter a number"))
if num %2 ==0:
    print("{} is even".format(num))
else:
    print("{} is odd".format(num))'''

#to check whether a cherecter is a vowel or not

'''ch=input("enter a character")
if ch in["a","e","i","o","u"]:
    print("{} is vowel".format(ch))
else:
    print("{} is not vowel".format(ch))'''


# to check whether a number is multiplyer of 3 as well as 5

num=eval(input("enter a number"))
if num%3==0 and num%5==0:
    print("{} is multiplyer of 3 and 5".format(num))
else:   
     print("{} is not multiplyer of 3 and 5".format(num))