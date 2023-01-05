#dictenery
"""d1={1:"abc",2:"def"}
print(d1)

d2={"EMP101":["Mohit kumar",5623521],"EMP102":["raman",89465123]}
print(d2)



print(d1[1])
print(d2["EMP102"])
#print(d1[56])

print(d1.get(1))
print(d2.get("EMP101"))
print(d1.get(56))
for k,v in d2.items():
    print(k,"=",v)"""



#
"""l1=[10,20,30,40]
l2=["abc","zxc","asd","qwe"]
d1=dict(zip(l1,l2))
print(d1)


d1=input("data1:")
l1=d1.split(",")

d2=input("data2:")
l2=d2.split(",")

z2=dict(zip(l1,l2))
print(z2)"""



#

"""da1=input("data1:")
da2=input("Data2:")
l1=da1.split(",")
l2=da2.split(",")
d1={}
if (len(l1)==len(l2)):
    for i in range(len(l2)):
        d1[l1[i]]=l2[i]
    print(sorted(d1.items()))
else:
    print("length should be equal")"""





#
"""a=input("data1:")
b=input("data2:")
c=a.split(",")
d=b.split(",")
dict1=dict(zip(c,d))
key=input("key:")
if key in dict1:
    print("value:",dict[key])
else:
    print("value:",dict1.get(key,"None"))"""





#pop------>print+delete





