#-- Pattern-1
for j in range(4):
    for i in range(4):
        print('* ',end="")
    print()
#-- Pattern-2
print()
for j in range(1,5):
    for i in range(j):
        print('* ',end="")
    print()
#-- Pattern-3
print()
for k in range(4):
    for i in range(4-k):
        print('* ',end="")
    print()