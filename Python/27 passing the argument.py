#passing the argument/parameter

"""def add(a,b):
    c=a+b
    print("sum is",c)
                             #calling function
add(56,151)
add(1546,456)"""



#write a function to calculate s.i witout passing argument
"""def si():
    p=eval(input("enter first number"))
    q=eval(input("enter secon number"))
    r=eval(input("enter third number"))
    intrest=p*q*r/100
    print("final number",intrest)

si()"""



#write a function to calculate s.i with passing argument
"""def si(p,q,r):
    intrest=p*q*r/100
    print("final number",intrest)

si(1200,4,5)"""



#write a function to find greater of 3 number by using function with argument

def greatest(a,b,c):
    if a>b and a>c:
        print("{} is greatest".format(a))
    elif b>c:
        print("{} is greatest".format(b))
    else:
        print("{} is greatest".format(c))


greatest(5,6,8)