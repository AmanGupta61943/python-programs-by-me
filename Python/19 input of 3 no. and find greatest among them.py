#input of 3 no. and find greatest among them
a,b,c=eval(input("enter three numbers"))
if a>b and a>c:
    print("{} is greatest".format(a))
elif b>c:
    print("{} is greatest".format(b))
else:
    print("{} is greatest".format(c))