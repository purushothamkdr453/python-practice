#--- unpacking and packing

def fun(a,b,c,d):
    print(a)
    print(b)
    print(c)
    print(d)

mylist = [1,2,3,4]

#-- The below function call will fail since we are passing the whole list which will be considered as single param instead of 4
#fun(mylist)

fun(*mylist) #-- unpacking

print("------")
for i in range(3,6):
    print(i)

print("------")

rangelist = [3,6]

for j in range(*rangelist): #-- unpacking
    print(j)


#--- Packing

print("------")

def printsum(*args):
    sum = 0
    for i in range(0,len(args)):
        sum = sum + args[i]
    return sum

print(printsum(1,2,3,4,5))

#-- both packing & unpacking

def func1(a,b,c):
    print(a)
    print(b)
    print(c)

def fun2(*args):
    args = list(args)
    args[0] = "purushotham"
    args[1] = "reddy"

    func1(*args)



fun2('hello','hi','hey')


#-- ** for dictionary unpacking

def printdict(a,b,c):
    print(a)
    print(b)
    print(c)

mydic = { "a":1,"b":2,"c":3 }
printdict(**mydic)

#--- packing of dictionary using **kwargs


def printdictvalues(**kwargs):

    print(type(kwargs))

    for key in kwargs:
        print("%s == %s" %(key,kwargs[key])

printdictvalues(
    
                
    
