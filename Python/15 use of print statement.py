#use of print statement

print("hello","world")
print("hello","world",sep="|")

print("hello","world",sep="|",end="***")
print("wellcome to programing")


#use of placeholder in print
a=12
b=34
print("a is() and b is ()".format(a,b))


#use of formate specifiers:starts with%

a=45
b=891
print("a is %d and b is %d"%(a,b))
print("a is %f and b is %f"%(a,b))

print("a is %4d and b is %4d"%(a,b))
print("a is %5d and b is %5d"%(a,b))


pi=3.14567
print("pi is %f"%pi)
print("pi is %.2f"%pi)


a=56
print("a in hexadecimal is%x"%a)
print("a in octal is%x"%a)