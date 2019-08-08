#--- we can create arrays in numpy in 6 ways
#-- array(),linspace(),logspace(),arange(),zeros(),ones()

from numpy import *

#--- creating arrays using array()

arr = array([1,2,3,4,5],int)
print(arr)
arr1= array([1,2,3,4,5.0])
print(arr1)
arr2 = array([1,2,3,4,5],float)
print(arr2)

print(arr2.dtype) #-- checking the data type

#--- creating arrays using linspace(), linspace divides into 1st and 2nd number into parts. it divides into (3rd number) times parts

arr = linspace(0,15,16)
print(arr)
arr = linspace(1,15,20)
print(arr)
arr = linspace(1,15) # Note: if you dont mention 3rd number then by default it divides into 50 parts
print(arr)

#----- creating an arrays using arange

arr=arange(1,15,2)
print(arr)

#---- creating an arrays using logspace

arr=logspace(1,15)

#---- creating an arrays using zeros
arr=zeros(5)
print(arr)
arr=zeros(5,int)
print(arr)

#---- creating an arrays using ones

arr=ones(5,int)
print(arr)
arr=ones(5,float)
print(arr)