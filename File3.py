from File1 import A


class C(A):

    def __init__(self):
        print("This is child class constructor")

    def cclassmethod(self):
        print("This is C class method")


obj = C()
obj1 = A()
obj.aclassmethod()
obj.cclassmethod()

