x = int(input("Please enter the number of candles you want"))
i = 1
av=5
while i <= x:
    if i > av:
        print("out of stock")
        break
    print("Candy")
    i+=1
print("Bye")