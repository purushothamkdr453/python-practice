#-- creating tuple

tuple1=()
print("printing empty tuple")
print(tuple1)

tuple1=('a',1,"helloworld")
print("printing tuple with multiple data types")
print(tuple1)

mylist = [ 1, 'a', "hello", 9+1 ]
print(tuple(mylist))

tuple1=(1,"Hey","Hello")
for i in range(5):
    tuple1=(tuple1,i)
print(tuple1)

#-- nested tuples

tuple1 = (1,'a','b','c')
tuple2 = (3,'c','h','f')
tuple3 = (tuple1,tuple2)
print(tuple3)

#-- repitition tuple
print(('hello',)* 3)

#--- builtin function

mytuple = tuple('Hello')
print(mytuple)

#-- concatenation using +

tuple1 = ( 'hello', 'Purushotham' )
tuple2 = ( 'Shell', 'Python' )
tuple3 =  tuple1 + tuple2
print(tuple3)

#-- slicing operation using :

tuple1 = tuple('reddys')
print(tuple1[2:])

print(tuple1[::-1])

print(tuple1[3:5])

#--- deleting the tuple

tuple2 = ( 'Hello', 1, 2+5 )
print(tuple2)

del tuple2
#print(tuple2)


