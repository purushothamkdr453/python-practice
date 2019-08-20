from math import factorial,sqrt
import math
import random
import time
from datetime import date
import operator

#------------- Math related functions
print(sqrt(16))
print(factorial(5))
print(math.fabs(-5))
print(math.ceil(2.2))
print(math.floor(2.2))
print(math.copysign(1,-2))
print(math.gcd(5,15))
print(math.log(2,3)) #-- log 2 value with base3
print(math.log2(2))
print(math.log10(20))
print(math.pow(2,3))
print(math.exp(2))
print(math.sin(30))
print(math.cos(60))
print(math.tan(45))
print(math.hypot(3,4))
print(math.degrees(60))
print(math.radians(60))
print(math.pi)
print(math.gamma(4))
print(math.e)

if math.isnan(math.nan):
    print("True : Not a number")
else:
    print("its a number")

if math.isinf(math.inf):
    print("True: infinite number")
else:
    print("not infinite number")
#------- Random related functions

mylist = [ 'purushotham', 'chandra', 'ravi' ]
print(random.randint(1,5))
print(random.random())
print(random.choice(mylist))
random.shuffle(mylist)

#--- Number of seconds from EPOCH time i.e from Jan1st 1970
print(time.time())

print(date.fromtimestamp(1565335861.4913108))

#------------- operator(Inplace) related functions --------------------

print(operator.iadd(2,3))
print(operator.isub(3,2))
print(operator.imul(3,2))
print(operator.itruediv(5,3))
print(operator.imod(5,3))
print(operator.iconcat('Purushotham','Reddy'))