
# oop class

class Test:
    def __init__(self,str):
        print("Constructor called")
        self.str=str
    def show(self):
        print("Hello World")
        print("str : ",self.str)

obj=Test("Ajay")super

obj.show()

print("\n ------------- Inheritance ------------- \n")

class parent:
    def show(self):
        print("Parent show method")
    def show1(self):
        print("Parent show1 method")

class child(parent):
    def show(self):
        super(child, self).show() #this will cal parent class's show()
        #print("Child show method")

e=child()
e.show1()
e.show()
#e1=parent()
#e1.show()
