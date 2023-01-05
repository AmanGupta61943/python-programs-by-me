"""try:
    print("Outter try block")

    try:
        print("Inner try block")
        print(10/0)
    except ZeroDivisionError:
        print("Inner except block")
    finally:
        print("Inner finally block")
except:
    print("outer except block")
finally:
    print("outter finally block")"""





"""try:
    fh=open("my.txt","r")
    print(fh.read())
except IOError:
    print("Error: cant find file or read data")
else:
    print("Content written successfuly")"""







"""def checkage(age):
    if age<0:
        raise ValueError("age should be greater than or equal to zero")
    print("age is valid")
try:
    age=int(input("age: "))
    checkage(age)
except ValueError as err:
    print(err.args)
finally:
    print("executed in any condition")"""









"""try:
    a=5
    b="0"
    print(a+b)
except TypeError:
    print("Unsupported operation")
print("out of try except blocks")"""



 
class OurException(Exception):
    def __init__(self,message):
        self.message=message
class UsingUserException:
    try:
        a=int(input("a: "))
        b=int(input("b: "))
        if b==0:
            raise OurException("b should be greater than 0")
        d=a/b
        print("division operation successful with result:",d)
    except OurException as err:
        print("user defined Exception:",err.message)


