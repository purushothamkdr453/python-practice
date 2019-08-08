class A:
    def __init__(self):
        print("in init A class")

    def greet(self):
        print('Hello Purushotham')

class B(A):
    def __init__(self):
        super().__init__()
        super().greet()
        print("in init B class")

b1=B()

#---- Note incase multiple inheritance, init function of super follows MRO(method resolution order)
#--- first in the sequence ( in left & right )

class AB:
    def __init__(self):
        print("in init A class")



class CD():
    def __init__(self):
        print("in init B class")



class EF(AB,CD):
    def __init__(self):
        super().__init__()

f = EF()