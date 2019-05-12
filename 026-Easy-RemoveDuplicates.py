#!/usr/bin/env python
import sys
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ll=len(nums)
        if ll<=1: return ll
        i=0
        j=1
        while j<ll and nums[i]!=nums[j]:
            i,j=j,j+1
        while j<ll:
            if nums[i]==nums[j]:
                j+=1
            else:
                i+=1
                nums[i]=nums[j]
                j+=1
        return i+1

try:
    n=list(map(int,sys.argv[1:]))
except:
    print('Program to sort a list of integers and remove any duplicate')
    print('Usage: %s <list of integers>'%sys.argv[0])
    sys.exit(-1)
s=Solution()
print('Original list:',n)
n.sort()
n1=len(n)
print('Sorted  list: ',n)
n2=s.removeDuplicates(n)
print('Removing duplicates, %i values were removed'%(n1-n2))
print('New   list:   ',n[:n2])
