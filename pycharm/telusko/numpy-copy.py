from numpy import *

#--- Vectorized operation

arr1 = array([1,2,3,4,5])
arr1 = arr1+5
print(arr1)

arr2 = array([2,3,4,5,6])
arr3 = arr1 + arr2
print(arr3)

#---- concatenate
print(concatenate([ arr1,arr2 ]))

#---- other basic operations

print(min(arr2))
print(max(arr2))
print(sin(arr2))
print(cos(arr2))
print(log(arr2))
print(sqrt(arr2))
print(sum(arr2))

#--- Copying array in 3 ways 1. normal 2. shallow copy 3. deep copy

#1. Normal copy. In Normal copy both the arrays store the data in same memory location
# inorder to store the date in different memory locations we use shallow copy and Deep copy

arr4 = arr3
print(arr3)
print(arr4)
print(id(arr3))
print(id(arr4))

#2. Shallow copy, using view function, we can make arrays store in different location
#-- also if we make change to first array that will reflect in 2nd array as well
arr5 = arr4.view()
arr4[0]=9
print(arr4)
print(arr5)
print(id(arr4))
print(id(arr5))

#3. Deep Copy- using copy funxtion, we can make arrays store in different locations
#-- also if we make change to first array that will not impact second array.

arr6=arr5.copy()
arr5[0]=10
print(arr5)
print(arr6)
print(id(arr5))
print(id(arr6))