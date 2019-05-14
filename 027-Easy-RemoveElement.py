#!/usr/bin/env python

import sys
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ll=len(nums)
        if ll==0: return 0
        done=True
        for i in range(ll):
            if nums[i]==val:
                done=False
                break
        if done: return ll
        for j in range(i+1,ll):
            if nums[j]!=val:
                nums[i]=nums[j]
                i+=1
        return i
if __name__=='__main__':
    try:
        myList=list(map(int,sys.argv[1:-1]))
        v=int(sys.argv[-1])
    except:
        print('Program to remove all instances of an item from a list')
        print('Usage: %s <list of integers> <value to remove>'%sys.argv[0])
        sys.exit(-1)
    s=Solution()
    n=s.removeElement(myList,v)
    print(myList[:n])
