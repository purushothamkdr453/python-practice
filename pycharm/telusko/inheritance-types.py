#--- Single level inheritance

class A:
    def func1(self):
        print("inside function-1")
    def func2(self):
        print("inside function-2")

class B(A):
    def func3(self):
        print("inside function-3")
    def func4(self):
        print("inside function-4")

b1=B()
b1.func1()

#----------- Multi-level inheritance -------------------

class A:
    def func1(self):
        print("inside function-1")
    def func2(self):
        print("inside function-2")

class B(A):
    def func3(self):
        print("inside function-3")
    def func4(self):
        print("inside function-4")

class C(B):
    def func5(self):
        print("inside function-5")

c1 = C()
c1.func1()
c1.func4()

#-----Multiple inheritance--------------------


class A:
    def func1(self):
        print("inside function-1")
    def func2(self):
        print("inside function-2")

class B():
    def func3(self):
        print("inside function-3")
    def func4(self):
        print("inside function-4")

class c(A,B):
    pass

c1 = c()
c1.func1()
c1.func3()