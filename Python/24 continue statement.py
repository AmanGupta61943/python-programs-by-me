#continue statement
for x in range(1,11):
    if x==4:
        continue
    print("hello",x)

 

#continue statement is used to skip the part of loop when some 
x=0
while x<10:
    x=x+1
    if x==4:
        continue
    print(x)



#condition got satisfied
for x in range(1,21):
    if x>=2 and x<=7:
        continue
    print("hello",x)