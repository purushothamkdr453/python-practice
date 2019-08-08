#--- Passing List to function
def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2 == 0:
            even+=1
        else:
            odd+=1
    return even,odd

mylist = [ 10, 11, 13, 12, 14]
even,odd = count(mylist)
print("Even : {} and Odd: {}".format(even,odd))

print("--------------------------------")

#---- Taking the list from user and passing it to function

ln = int(input("Enter the length of the list"))
lst = []
for i in range(ln):
    ele = int(input("Enter the value"))
    lst.append(ele)

print(lst)

def count1(lst):
    ev=0
    od=0
    for i in lst:
        if i%2 == 0:
            ev+=1
        else:
            od+=1
    return ev,od

ev,od = count1(lst)
print("Even : {} and Odd: {}".format(ev,od))