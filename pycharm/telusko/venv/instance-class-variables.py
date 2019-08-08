class car:
    #-- Class variable, also known as static variable
    wheels  = 4

    def __init__(self):
        #--- Instance variables
        self.com = 'BMW'
        self.mil = 10


c1 = car()
c2 = car()
#--- changing the instance variable
c1.mil=12

#--- changing class variable

car.wheels = 5

print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,c2.wheels)