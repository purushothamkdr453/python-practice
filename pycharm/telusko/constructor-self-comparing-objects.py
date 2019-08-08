class computer:
    #--- __init__ method is a constructor
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def compare(self,other):
        if self.ram == other.ram:
            return True
        else:
            return False

c1 = computer('i3',16)
c2 = computer('i5',8)
c1.ram=8

#--- Comparing objects, compare is not built-in function

if c1.compare(c2):
    print("objects are same")
else:
    print("objects are not same")



