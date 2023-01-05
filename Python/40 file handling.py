#using open method
"""f= open("my.txt","w")   #writng purpose4
f.write("this is my file")
f.close()



#
f=open("studen.txt","w")
r=(input("Enter roll no.: "))
n=input("name: ")
f.write(r)
f.write(n)
f.close()"""

#r mode----------)reading purpose
"""f=open("my.txt","r")
str1=f.read()
print(str1)



f=open("my.txt","r")
for x in f:
    print(x)"""

#write a program to copy the content of one file to another

"""f=open("my.txt","r")
x=open("copy.txt","w")
str1=f.read()
x.close()
f.close()"""



#write a program to append the content of one file to another

"""f=open("my.txt","r")
x=open("copy.txt","a")
str1=f.read()
x.close()
f.close()"""


#wrie a program to open a                                                 count line,word,charater
lines=0
words=0
char=0
f=open("my.txt")
for x in f:
    lines=lines+1
    words=words+len(x.split(","))
    char=char+len(x)
print("lines",lines)
print("words",words)
print("char",char)