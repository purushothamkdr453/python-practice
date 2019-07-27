"""
Sample Python function to check
whether the element is even or odd
"""
def check(x):
    if(x % 2 == 0):
        print("even")
    else:
        print("odd")

check(3)
check(2)

#--- Default Arguments

def defaultarguments(x,y=50):
    print("Value of x is", x)
    print("value of y is", y)

defaultarguments(10)

#-- Keyword arguments

def name(firstname,lastname):
    print(firstname,lastname)

name(firstname="Purushotham",lastname="Reddy")
name(lastname="Reddy",firstname="Purushotham")

#-- Variable length arguments

def variablelengtharguments(*argv):
    for arg in argv:
        print(arg)

variablelengtharguments('Hello','Purushotham','Reddy')

#-- keyword arguments for variable number of keyword arguments

def kwarguments(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" %(key,value))
kwarguments(fname="Kadiri",mname="Purushotham",lname="Reddy")

#-- creating anonymous functions using lambda

cube = lambda x : x*x*x
print(cube(7))


def test(x):
    x[0] = 20

mylist = [10,0,9,90]
test(mylist)
print(mylist)


def test1(x):
    x = [10,20,30]

mylist1 = [40,50,60]
test1(mylist1)
print(mylist1)

def test2(x):
    x = 20

x = 10
test2(x)
print(x)
        
