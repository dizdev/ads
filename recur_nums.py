import random
from time import time

def req_sort(nums):
    if len(nums) <=1: #kluczowy warunek, gdy lista juz jest liczba, zwracamy liczbe, scalamy dwie listy
        return nums
    
    mid = len(nums)/2
    sort_left = req_sort(nums[:mid])
    sort_right = req_sort(nums[mid:])
    return merge(sort_left, sort_right)


def merge(left, right):
    result = []
    i = j = 0
    
    while i<len(left) and j < len(right):
        if left[i]>=right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
    while i<len(left) and j == len(right):
        result.append(left[i])
        i += 1
    while i == len(left) and j<len(right):
        result.append(right[j])
        j += 1
    return result
            
        
if __name__=="__main__":
    start = time()
    nums = random.sample(xrange(0,50000),10000)
    req_sort(nums)
    end = time()
    print (end-start)
