def update(x):
    print(id(x))
    x = 8
    print(id(x))
    print(x)

a=10
print(id(a))
update(a)
print(a)

print()
print()

def updatelist(lst):
    print(id(lst))
    lst[1] = 25
    print(id(lst))
    print(lst)

mylist = [ 10, 20, 30, 40 ]
print(id(mylist))
updatelist(mylist)
print(mylist)
