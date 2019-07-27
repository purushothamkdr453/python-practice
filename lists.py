#-- creating a list

mylist = []
print("printing the empty list")
print(mylist)

#-- adding element to the list

mylist=['purushotham']
print("adding element to the list")
print(mylist)

#-- Adding multiple elements to the list

mylist=['hello','purushotham','reddy']
print('adding multiple elements to the list')
print(mylist)

#-- adding lists to lists

mylist=[['hello','purushotham'],['reddy']]
print("adding lists to lists")
print(mylist)

#--- creating a list with duplicate values

mylist=['h','p','h','w','l','p','n','w']
print("creating a list with duplicate values")
print(mylist)

#--- creating a list with mixed type of values

mylist=['a',1,"purushotham",7+10]
print("creating a list with mixed type of values")
print(mylist)

#--- adding elements to list

mylist=[]
print("printing empty list")
print(mylist)

mylist.append(1)
mylist.append(2)
mylist.append(4)
print(mylist)

for i in range(1,4):
    mylist.append(i)
print(mylist)

mylist.append((5,6))#adding tuple to list
print("adding tuple to list")
print(mylist)

mylist2=['hello','purushotham']
mylist.append(mylist2)
print("appending list to list")
print(mylist)

mylist2.insert(0,'Reddy')
print(mylist2)
mylist.insert(3,'Accenture')
print(mylist)

# adding multiple elements at the end of the list using extend

mylist.extend([8,'hey','wow'])
print(mylist)

#-- Accessing the elements of list using indexes
mylist=["Hello","Puruhsotham","Reddy"]
print(mylist[0])
print(mylist[2])

mylist=[['Hello','purushotham'],['reddy']]
print(mylist[0][1])
print(mylist[1][0])

mylist=[1,'hello','puru','reddy',8+17]
print(mylist[-1])
print(mylist[-3])

#-- Removing the elements using remove and pop method

mylist=[1,2,3,4,5,6,7,8,9]
mylist.remove(5)
mylist.remove(6)
print(mylist)

for i in range(1,5):
    mylist.remove(i)
print(mylist)

mylist.pop()
print(mylist)

mylist.pop(1)
print(mylist)

#-- slicing using :

mylist = ['h','e','y','z','l','k','b','r','x','q','w','d']

print(mylist[3:7])
print(mylist[5:])
print(mylist[:-6])
print(mylist[:]) # printing whole list
print(mylist[::-1])# printing the elements in reverse order

#--- to check all the functions supported by list type
print(dir(list))


