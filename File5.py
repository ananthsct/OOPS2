from File1 import A
from File2 import B
from File3 import C


class D(A,B,C):
    def dclassmethod(self):
        print("This is D class method")


obj = D()
obj.aclassmethod()
obj.bclassmethod()
obj.cclassmethod()
obj.dclassmethod()

obja = A()
obja.aclassmethod()
