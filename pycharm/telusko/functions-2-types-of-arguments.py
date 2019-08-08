#-- Actual Arguments -> Arguments passed in the function call
#---- Formal arguments -> arguments in the function definition
#--- Actual Arguments can be of 4 types -> position, default,keyword, variable length

def person(name,age): #--Formal Paramaters
    print(name)
    print(age)

person('Purushotham',28) #--- Actual arguments of position type

person(age=27,name='Chandra') #-- Actual arguments of keyword type

#---- Actual arguments of default type

def person1(name,age=10): #--- default type
    print(name)
    print(age)

person1('Purushotham',28)

#------ variable length arguments

def sum(a,*b):
    c = a
    print(type(a))
    print(type(b))

    for i in b:
        c = c + i
    print(c)

sum(10,20,30,40)
