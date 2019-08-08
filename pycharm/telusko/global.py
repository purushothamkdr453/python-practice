#----- Function-1

a = 10 #Global scope
def print_check(a):
    a=8 #local scope
    print("inside function",a)

print_check(a)
print("outside function",a)
print("function-1 ended")
#----------- Function-2
#--- Inorder to change the global variable value we use global keyword
#--- limitation with global keyword is we can not use same variable in both in & outside function. to overcome this we use globals()

a = 10
def print_check():
    global a
    a = 20
    print("inside function",a)

print_check()
print("outside function",a)
print("function-2 ended")


#------ Function-3
#--- to use the same variable in both inside function and outside function we use globals()
b=10
def print_check():
    x=globals()['b']
    print(id(x))
    globals()['b']=15
    b = 20
    print("function local value is",b)

print(id(b))
print_check()
print("outside function value is ",b)