import array

vals = array.array('i',[1,10,8,9,-2])
print(vals)

#--- buffer info method

print(vals.buffer_info())

#--- typecode check

print(vals.typecode)

#--- reverse

vals.reverse()
for i in vals:
    print(i)

#-- printing array

print()
for i in range(len(vals)):
    print(vals[i])

#-- creating a new array from existing one
print()
nvals = array.array('i',[2,4,6,8])
dvals = array.array(nvals.typecode,(a*a for a in nvals))
for i in dvals:
    print(i)

#-- while loop to print array values
print()
i=0
while i < len(dvals):
    print(dvals[i])
    i+=1