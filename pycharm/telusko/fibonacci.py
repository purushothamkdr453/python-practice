fn = int(input("Please enter length of fibonacci series : "))

#------- Fibonacci series -1

def fibonacci(n):
    if n <= 0:
        print("Number is negative number")
    elif n == 1:
        a=0
        print(a)
    else:
        a=0
        b=1
        print(a)
        print(b)
        for i in range(2,fn):
            c = a + b
            a = b
            b = c
            print(c)

fibonacci(fn)

#------- Fibonacci series -2




