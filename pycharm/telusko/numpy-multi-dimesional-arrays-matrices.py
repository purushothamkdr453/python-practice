from numpy import *

arr1 = array([
                [1,2,3,4,5],
                [2,4,5,6,7]
            ])

#--- type of array

print(arr1.dtype)

#---- printing the dimensions of the array

print(arr1.ndim)

#---- printing the no of rows & columns

print(arr1.shape)

#--- printing the size of array i.e no of elements in the array

print(arr1.size)

#--- converting the 2 dimesional array into single dimensional array
print(arr1.flatten())

#---- converting the single dimensional array into multi-dimensional

print(arr1.reshape(5,2))

#---- creating matrix from arrays

arr1 = array([
                [1,2,3],
                [2,4,5],
                [6,7,8]
            ])

m = matrix(arr1)
print(diagonal(m))

print(m.min())
print(m.max())

m2 = matrix('1 2 4;4 5 6;7 8 9')
print(m)
print(m2)

print(m+m2)
print(m*m2)