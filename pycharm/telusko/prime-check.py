num = int(input("Please enter the number, we will tell you whether it is prime ot not : "))

if num > 1:
    for i in range(2,num):
        if num%i == 0:
            print(num," is not a prime number")
            print(i,"times",num//i,"equal to",num)
            break
    else:
        print(num," is a prime number")
else:
    print(num,"is not a prime number")