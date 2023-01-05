#class book
"""class book:
    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.price=price
    def show(self):
        print(self.id,self.name,self.price)
b1=book(101,"python",250)
b1.show()"""


#
"""class student:
    def get_info(self):
        self.reg=input("Enter reg no. :")
        self.name=input("enter Name :")
    def show_info(self):
        print(self.reg,self.name)"""



"""class result(student):
    def get_result(self):
        self.marks=int(input("Enter Marks"))
    def show_marks(self):
        print(self.marks)
r=result()
r.get_info()
r.show_info()
r.get_info()
r.get_result()
r.show_marks()"""




#
"""class employee:
    def get_info(self):
        self.id =input("Enter id: ")
        self.name=input("Enter name: ")
    def show_info(self):
        print(self.id,self.name)


class salary:
    def get_acc(self):
        self.sal=eval(input("Enter sal: "))
        self.ben=eval(input("Enter ben"))
    def show_acc(self):
        print(self.sal+self.ben)

class calculate(employee,salary):
    pass
c=calculate()
c.get_info()
c.show_info()
c.get_acc()
c.show_acc()"""




#
"""class A:
    def __init__(self):
        print("inparent.class")
class B(A):
    def __init__(self):
        super().__init__()
        print("inChildClass")
ob=B()"""


#private attribute and privet method
class student:
    __reg=""
    __name=""
    def __get_info(self,r,n):
        self.__reg=r
        self.__name=n
    def show_info(self,r,n):
        self.__get_info(r,n)
        print(self.__reg,self.__name)
s=student()
s.show_info("112218801","aman")


