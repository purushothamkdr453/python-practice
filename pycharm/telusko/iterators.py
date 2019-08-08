nums = [ 1,2,3,4 ]
#for i in nums:
    #print(i)

#--- creating iterator object by passing list to iter function
it = iter(nums)

print(it.__next__())
print(it.__next__())
print(it.__next__())
#--- another way of using iterator is using next
print(next(it))
