import random
from time import time

def quickSort(a):
    if len(a) <= 1:
        return a
    else:
        less = []
        more = []
        pivot = random.choice(a)
        for i in a:
            if i < pivot:
                less.append(i)
            if i > pivot:
                more.append(i)
        less = quickSort(less)
        more = quickSort(more)
       
        return less + [pivot] + more

if __name__=="__main__":
    start = time()
    nums = random.sample(xrange(0,50000),10000)
    quickSort(nums)
    # nums.sort()
    end = time()
    print (end-start)
