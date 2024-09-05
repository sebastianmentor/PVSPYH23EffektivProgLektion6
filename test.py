from functools import reduce

l = [2,3,1,4,5]


def negate(num:int) -> int:
    return -num

l.sort(key=negate)
print(l)
#[1,2,3,4,5] <-- 0
#[-5,-4,-3,-2,-1] <-- rests 
#[5,4,3,2,1] <-- 1

sorter_master = lambda l,f: l.sort()

print(sorter_master(l,negate))

print(l)
print([x for x in l if x> 3])
print([x for x in list(filter(lambda x:x if x>3 else None, l))])
print([x for x in list((lambda x:x if x>3 else None, l))])
print(reduce(lambda x,y: x+y, l))
print(sum(l))
