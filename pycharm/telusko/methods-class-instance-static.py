class student:

    school = 'Manikanta'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3


    #--- Instance Method
    def printmarks(self):
        print(self.m1,self.m2,self.m3)

    #-- class method
    @classmethod #--- Classmethod decorator
    def getschoolname(cls):
        print(student.school)

    #--- static method
    @staticmethod #-- static method decorator
    def info():
        print("we love manikanta vidyanikethan")

s1 = student(10,20,30)
s2 = student(40,50,60)

#-- calling object method
s1.printmarks()
s2.printmarks()
#-- calling class method
student.getschoolname()
#---calling static method
s1.info()
student.info()
