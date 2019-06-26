#!/usr/bin/env python

import sys
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i=0
        for v in nums:
            if v>=target:
                return i
            i+=1
        return i
try:
    myList=list(map(int,sys.argv[1:-1]))
    value =int(sys.argv[-1])
    print ('Value to search is %i'%value)
    print ('List is:', myList)
    S=Solution()
    print('Value %i is present or could be inserted at index %i'%(value, S.searchInsert(myList, value)))
except:
    print('Program to find the index of a value in a sorted array or to find at which index to insert it')
    print('Usage:\n%s <sorted list of integers> <integer value to search>'%sys.argv[0])

