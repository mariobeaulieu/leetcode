#!/usr/bin/env python

import sys
from typing import List

class Solution:
    def search(self, nums: List[int], t: int) -> int:
        debug=True
        n=len(nums)
        if n==0:           return -1
        elif n==1:
            if nums[0]==t: return 0
            else:          return -1
            # Find pivot (smallest of all values)
        delta=n
        i0=0
        while delta>1:
            delta = (delta+1)//2
            i1    = (i0+delta)%n
            if debug: print('v[i0]=%i, v[i1]=%i, delta=%i'%(nums[i0],nums[i1],delta))
            # If value at i0 is less than at i1, it means the pivot is at or after i1
            if nums[i0]<nums[i1]: i0=i1
        i0=(i1+1)%n
        if nums[i1]<nums[i0]: i0=i1
        if debug: print('Pivot found at position %i'%i0)
        # Now find value t
        if t<nums[i0] or t>nums[i0-1]: return -1
        if t==nums[i0]: return i0
        if t==nums[i0-1]: return (i0-1)%n
        delta=n
        pivot=i0
        while delta>1:
            delta=(delta+1)//2
            if i0<pivot and i0+delta>=pivot: delta=pivot-i0-1
            i1   =(i0+delta)%n
            if   debug: print('v[i0]=%i, v[i1]=%i, delta=%i'%(nums[i0],nums[i1],delta))
            if   t> nums[i1]: i0=i1
            elif t==nums[i1]: return i1
        if nums[i0]==t: return i0
        if nums[i1]==t: return i1
        return -1
                
try:
    n=list(map(int, sys.argv[1:-1]))
    t=int(sys.argv[-1])
except:
    print('\nProgram to find a value in a sorted rotated array')
    print('\nUsage: %s <rotated sorted array values> <value to search>'%sys.argv[0])
    print('\nExample:\n  %s 5 6 7 1 2 3 4 2'%sys.argv[0])
    print('Would search value 2 in rotated array 5 6 7 1 2 3 4\n-1 is returned if value is not found.')
    sys.exit(-1)
s=Solution()
print(s.search(n,t))
