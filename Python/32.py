#  min max
"""data=input("data: ")
list1=data.split(",")
size=len(list1)
for i in range (size):
    list1[i]=int(list1[i])
max_val=max(list1)
min_val=min(list1)
print("min:",min_val)
print("max:",max_val)
difference=max_val-min_val
print("difference:",difference)"""

#


"""a=input("data:")
b=a.split(",")
c=len(b)
for i in range(c):
    b[i]=int(b[i])
s=sum(b)
print("list1",b)
print("sum:",s)
for i in range(c):
    b[i]=b[i]*b[i]
print("square:",b)
print("sum of square",sum(b))"""






#
"""a=input("data:")
b=a.split(",")
c=len(b)
for i in range(c):
    b=int(b[i])
print("list:",b)
find=int(input("num:"))
for i in range(0,len(b)-1):
    if b[i]==find:
        if b[i+1]==find:
            prsult="True"
            break
    else:
        result="False"
print(result)"""                                                                      """    ni huwaaa"""





#program to creat new list of odd and even list


"""a=input("data:")
b=a.split(",")
size=len(b)
for i in range(size):
    b[i]=int(b[i])
c=[]
for i in range(0,len(b)):
    if(not i%2==0):
        c.append(b[i])
print("odd index element:",c)"""



#assending or dessending
a=input("data:")
b=a.split(",")
c=len(b)
for i in range(c):
    b[i]=int(b[i])
if b==sorted(list(b)):
    print("True")
else:
    print("false")