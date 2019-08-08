from array import *

#-- Taking the array values from user

arr =  array('i',[])

len = int(input("Enter the length of the array"))

for i in range(len):
    x = int(input("Enter the value"))
    arr.append(x)

print(arr)

#-- getting the index based on the value entered using in-built function

val = int(input("Enter the number for which u want to find index"))

print(arr.index(val))

#---- getting the index based on the value entered manually

k=0
for i in arr:
    if i == val:
        print(k)
        break
    k+=1