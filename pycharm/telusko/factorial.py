n = int(input("Enter the number for which you want to find factorial : "))

def fact(n):
    a = 1
    for i in range(1,n+1):
        a = a*i
    return a

result = fact(n)
print(result)