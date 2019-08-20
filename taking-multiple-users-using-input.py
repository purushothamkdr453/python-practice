#---- Taking multiple inputs from user using split function

x,y = input("Enter two values ").split()
print("First value : ", x)
print("Second value : ", y)

x,y,z = input("Enter two values ").split()
print("First value : ", x)
print("Second value : ", y)
print("Third value : ", z)

x,y = input("Enter two values ").split()
print("Firt value is {} and second value is {} ".format(x,y))

mylist = list(map(int,input("Enter values").split()))
print(mylist)

#--------- Using List Comprehension

x,y = [ int(x) for x in input("enter 2 values : ").split()]
print("First value : ",x)
print("First value : ",y)

x,y,z = [ int(x) for x in input("enter 3 values : ").split()]
print("First value : ",x)
print("First value : ",y)
print("First value : ",z)

x,y = [ int(x) for x in input("enter 2 values : ").split()]
print("First value is {} and second value is {}".format(x,y))

mylist = [ int(x) for x in input("multiple values : ").split()]
print(mylist)






