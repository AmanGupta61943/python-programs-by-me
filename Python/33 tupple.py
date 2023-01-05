"""l1=[1,2,3,4,5]
print(l1)
tuple1=tuple(l1)
print(tuple1)


tuple2=tuple((input("enter element of tuple").split()))
print(tuple2)

data1=input("Data1:")
list2=data1.split(",")
tuple3=tuple(list2)
print(tuple3)"""

"""data=input("Data:")
list=data.split(",")
tuple1=tuple(list)
print("List:",list)
print("Tuple",tuple1)
index=int(input("Index:"))
if index<len(tuple1) and index>=-len(tuple1):
    print(tuple1[index])
else:
    print("enter valid index")"""



"""t1=tuple(input("Data:").split(","))
value=int(input("Value:"))
print("Tuple*",value,t1*value)
t2=tuple(input("Data2:").split(","))
print("result:",t1+t2)"""




#
"""t1=tuple(input("Data").split(","))
v1=input("Value:")
if v1 in t1:
    print("True")
else:
    print("False")"""





#tuple and list ;;;; list can be change while in tuple\
"""t1=(1,2,3,4,[5,6,7])
print(t1)
t1[4][1]="6 kaha gaya"
print(t1)

#delet tuple[0]

del t1
print(t1)
"""


"""data=input("Data:")
l1=data.split(",")
t1=tuple(l1)
index=int(input("Index:"))
l2=[]
if index<len(l1) and len(l1)>=-index:
    value=input("value:")
    l2=list(t1)
    l2[index]=value
    t2=tuple(l2)
    print("Tuple:",t2)
else:
    print("enter valid")"""





#



"""

data=input ("data:")
list1=data.split (",")
tuple1=tuple (list1)
print("tuple:",tuple1)
index=int (input ("index: "))
size=len (tuple1)
if index!=-1:
    if index<len (tuple1) and index>=-(size):
        tuple2=tuple1[:index]+tuple1[index+1:]
        print("after removing:",tuple2)
    else:
        print("enter valid index")
else:
    print ("after removing:", tuple1 [:index])
"""




#comparision of tuple
"""t1=tuple(input("tuple1:").split(","))
t2=tuple(input("tuple2:").split(","))
if t1==t2:
    print("True")
else:
    print("False")"""





#
"""
data=input("Data:")
l1=data.split(",")
val=input("element:")
t1=tuple(l1)
if val in l1:
    l1.remove(val)
    t2=tuple(l1)
    print("before detaction:",t1)
    print("after detaction:",t2)
else:
    print("enter existaed element")"""





#
