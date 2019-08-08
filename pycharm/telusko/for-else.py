#-- for-else loop
#-- break is compulsary when u are using for-else, to understand better comment break statment and execute the code

nums = [ 11, 12, 15, 16, 21 ]

for i in nums:
    if i%5==0:
        print(i)
        break
else:
    print("not found")
