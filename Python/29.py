"""str1=input("str1")
l1=str1.split()
print("list:",l1)

l2=[1,2,3,4,5,"abc","vgyd"]
print(12)

l1=list(input("str1").split())
print(l1)"""


#

"""l1=[1,2,3,4,5,6,7,8,9,10]
print(l1)
l1[2]="abc"
print(l1)



l2=[1,2,3,4,5,["abc",7,8]]
print(l2[0])
print(l2[5])
print(l2[5][1])"""



#
"""l1=[1,2,3,4,5,6,7,8,9,10]
print(l1[1:4])
print(l1[::])
print(l1[::-1])
print(l1[-1:-9:-1])
print(l1[0:9:2])
for x in l1:
    print(x)"""




#
"""data=input("data:")
list1=data.split(",")
print("list:",list1)
index=int(input("index:"))
if index<len(list1) and index>=(len(list1)):
    print("element:",list1[index])
else:
    print("invalid")"""



#use of append function


"""l1=[1,2,3,4,5]
print(l1)
l1.append("abc")
print(l1)
l1.append([5,6,7])
print(l1)
l1.append([8,9,10])
print(l1)"""



#
"""a=(input())
b=3
if (b==3) or (b[-1]==3):
    print("true")
else:
    print("false")"""


#


"""a=(input())
b=a.split(",")
if b==[0]==b[-1]:
    print("equal")
else:
    print("not equal")"""



"""data=input ("data:")
list1=data.split (",")
if list1[0]==list[-1]:
    print ("equal")
else:
    print ("not equal")"""


#


"""a=input("data: ")
b=a.split(",")
print("befor",b)
c=int(input("index: "))
if c<len(b) and c>=(len(b)):
    value=input("element: ")
    b[c]=value
    print("after",b)
else:
    print("invalid")"""


#

data=input("data: ")
list1=data.split(",")
size=len(list1)
for i in range(size):
    list1[i]=int(list1[i])
print(list1)
if list1[0] < list1[-1]:
    print("largest among first and last:",list1[-1])
else:
    print("largest among first and last:",list1[0])