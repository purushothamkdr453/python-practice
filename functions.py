#-- Required arguments
def printme(str):
    "This functions expects the required number of arguments to be passed"
    print(str)
    return;

printme("Purushotham")

#-- keyword arguments

def keywordarguments(name,age):
    "This function expects the keyword arguments to be passed"
    print("My name is" + name + " and my age is " + age)
    return;

keywordarguments(age='28',name="purushotham")

#--- Default arguments

def defaultarguments(name,age='28'):
    "This function expects the default arguments to be passed"
    print("my name is ", name + " my age is ", age)
    return;

defaultarguments("Purushotham")

#--- Variable length arguments

def variablelengtharguments(*argv):
    "variable length arguments using argv"
    for arg in argv:
        print(arg)

variablelengtharguments('purushotham','chandra','ravi')

#--- variable length arguments using kwargs

def kwarguments(**kwargs):
    for key,value in kwargs.items():
        print("%s == %s" %(key,value))

kwarguments(Name='Purushotham',age='28')


#--- anyonumous functions

sum = lambda x,y : x+y
print(sum(10,20))


#-- pass by reference

def printlist(mylist):
    mylist.append([1,2,3])
    print("Value inside function ",mylist)
    return mylist

mylist = [ 10,20,30]
printlist(mylist)
print("Value outside funtion ", mylist )

def printlist1(mylist):
    mylist=[1,2,3]
    print("Value inside function ", mylist)
    return 

mylist = [10,20,30]
printlist1(mylist)
print("Value outside funtion is ", mylist)

#--- local & Global variavles

total = 0

def sum(x,y):
    print("Value inside function is ", x+y)
    return

sum(10,20)
print("Value outside function is ", total)




