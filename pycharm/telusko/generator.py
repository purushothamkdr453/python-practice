#----- Generator is used to create iterators instead of using __iter__ and __next__ functions

def square():
    n = 1
    while n <= 10:
        sq = n*n
        yield  sq
        n+=1

sqvalues = square()

print(sqvalues.__next__())

for i in sqvalues:
    print(i)


