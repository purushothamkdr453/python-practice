num = int(input("Enter the number for which you want to find the factorial : "))

def fact(i):
    if i == 0:
        return 1

    return i * fact(i-1)


result=fact(num)
print(result)