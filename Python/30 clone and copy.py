#copy

"""a=[1,2,3,4,5]
b=a
print(a)
print(b)
print(a is b)
a[0]=56
print(a)
print(b)




# cloning
a=[7,8,9,56,78,90]
b=a[:]
print(a is b)
a[0]=89
print(a)
print(b)






#
a=input("data1 ")
x=a.split(",")
b=input("data2 ")
y=b.split(",")
if x[0]==y[0] or x[-1]==y[-1]:
    print("true")
else:
    print("false")"""




#
a=input("data: ")
x=a.split(",")
y=[]
for i in range(len(x)):
    if x[i] not in y:
        y.append(x[i])
print(x)
print("after removing duplicate:",y)






