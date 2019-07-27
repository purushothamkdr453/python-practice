num = int(input("Please enter the number for which you want to find out factorital : "))
#print(type(num))

def factorial(num):
    f = 1
    for i in range(1,num+1):
        f = f * i
    return f
        
result  = factorial(num)
print("result is ", result)


