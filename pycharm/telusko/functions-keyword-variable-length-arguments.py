#--- Keyword variable length arguments

def person(name,**data):
    print(name)
    print(data)

    for i,j in data.items():
        print(i,j)

person('Purushotham',age=28,city='Bengaluru',mob=9883819101)