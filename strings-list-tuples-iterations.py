#-- Strings are immutable
name = "hello purushotham"
print(name)
name = 1
print(name)

#name[0] = 'w'
#print(name[0])

print(id(name))

#-- Lists are mutable

List = [ 1, "hello", 1+2 ]
print(List)
List.append(10)
print(List)
List.pop()
print(List)
print(List[1])

#-- tuples are same as List, however these are immutable & faster than Lists

tup = ( 1, "Wow", 1+2 )
print(tup[1])
#tup[1]="Hello"

#-- Iterations using while & for
#-- iterations are done for both strings & lists apart from conditions

i=1
while(i<10):
    i+=1
    print(i)

for i in range(0,10):
    print(i)

message = "Hello World"
for i in message:
    print(i)

mylist = [ 1, "hello", 1+10 ]
for i in mylist:
    print(i)s


