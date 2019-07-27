name="Purushotham"

def globalvarprint():
    global name
    print("inside function ",name)
    name="Chandra"

print(name)
globalvarprint()
print(name)
