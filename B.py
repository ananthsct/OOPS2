from A import parentClass


class childClass(parentClass):

    def sub(self, a, b):
        print(b-a)          # overriding prent method

    def mul(self, a, b):
        print(a*b)
