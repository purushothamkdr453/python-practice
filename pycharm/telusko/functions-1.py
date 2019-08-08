#---- Function that greets

def greet():
    print("Hello")
    print("Good Morning")

greet()

#------- Function that returns values

def add(x,y):
    return x+y

result = add(5,5)
print(result)

#------ Function that returns multiple values

def add_sub(x,y):
    c = x +y
    d = x - y
    return c,d

result1,result2=add_sub(6,5)
print(result1)
print(result2)