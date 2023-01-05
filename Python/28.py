str1=input("code")
str2=input("tantra")
print("result",str1+str2+str2+str1)




#program to remove a character from string

str1=input("hello fucker")
print=str1[0:2]+str1[6:10]



#

str1=input("1: ")
str2=input("2: ")
str3=(str1[1:]+str2[1:])
if len(str3)==0:
    print("null")
else:
    print("output",str3)





#$
str1=input("1: ")
print(str1*4)
a=(3* str1[::-1])
print(a)





#


str1=input("1: ")
a=str1[0:3]
if len(str1)<3:
    print(str1)
else:
    print(a)
    


#


str=input("1: ")
num=int(input("num:"))
if num>len(str)or num<0:
    print("no. should be positive,less then the length of str")
else:
    print("ok")






#


a="welcome to python"
print(a.capitalize())
print(a.upper())
print("HELLO".lower())
print("HELLO".swapcase())
str1=input("enter few strings")
list1=str1.split(".")
print(list1)

str2="hello"
print(str2.center(10,"*"))




#


str1=("book")
str2=("school")
print(str1*3+str2)