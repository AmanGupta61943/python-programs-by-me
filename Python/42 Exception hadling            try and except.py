#Exception hadline
"""a=int(input("Enter a:"))
b=int(input("Enter b:"))
try:
    c=a//b
    print("Division is",c)
except:
    print("Program ends here")"""






"""l1=[12,23,34,45,56,67]
try:
    index=int(input("Enter index to print :"))
    print(l1[index])
except:
    print("Not a valid index")
print(l1)"""






"""def fun(a):
    if a<4:
        #throws ZeroDivisionError for a=3
        b=a/(a-3)
    #throws NameError if a>=4
    print("Vslue of b=",b)

try:
    fun(3)
    fun(5)

#note that braces()are necessary here for
#multiple exceptions
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handle")
except NameError:
    print("NameError Occurred and Handle")"""











"""marks={"Rahul":50, "Harsh":60, "Suresh":70}
name=input("Enter name: ")
try:
    print("marks:",marks[name])

except KeyError:
    print("name: {} not in the list".format(name))
print("End of the program")"""







"""try:
    a = int (input ("a: "))
    b = int (input ("b "))
    c = a + b
    d= a / b
    e = a * b
    print ("try successful")
except ZeroDivisionError:
    print ("zero division error occurred")
except NameError:
    print ("name error occurred")
except Exception:
    print ("exception occurred")"""









try:
    print ("outer try block")
    try:
        print ("Inner try block")
    except ZeroDivisionError:
        print ("Inner except block")
    finally:
        print ("Inner finally block")
except:
    print ("outer except block") 
finally:
    print ("outer finally block")