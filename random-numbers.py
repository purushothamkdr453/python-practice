import random
secret_number = random.randint(1,500)
#print(secret_number)

while True:
    res = int(input("Enter the secret value between 1 and 500 : "))
    if res==secret_number:
        print("You Won")
        break
    else:
        print("You loose")
        continue