#!/usr/bin/env python

import sys
from typing import List

class Solution:
    def nextPermutation(self, nums:List[int]) -> None:
        n=len(nums)
        if n<2: return
        # From the end, find the first value whose value is <
        for i in range(-1,-n,-1):
            if nums[i-1]<nums[i]:
                # find the first value from the end that is greater than nums[i-1]
                v=nums[i-1]
                for j in range(-1,i-1,-1):
                    if nums[j]>v:
                        nums[j],nums[i-1]=v,nums[j]
                        # values from nums[i] to nums[-1] need to be reversed
                        for k in range((1+i)//2,0):
                            #print('Flipping %i and %i'%(nums[i-1-k],nums[k]))
                            nums[i-1-k],nums[k]=nums[k],nums[i-1-k]
                        return
        nums.sort()
try:
    nums=list(map(int,sys.argv[1:]))
except:
    print('Usage: %s <list of integers>'%sys.argv[0])
    print('The program will find the next permutation greater than the current one')
    print('If impossible, the sorted list is returned')
    sys.exit(-1)
s=Solution()
print ('Initial list:    ',nums)
s.nextPermutation(nums)
print ('Next permutation:',nums)
