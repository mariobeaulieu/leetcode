#!/usr/bin/env python

import sys
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # The idea is to see how far each position would get me
        maxPos=0
        ll=len(nums)
        ll1=len(nums)-1
        for i in range(ll):
            if i>maxPos: return False
            m=i+nums[i]
            if m>maxPos: maxPos=m
            if m>=ll1: return True
        return False
    def canJump_old(self, nums: List[int]) -> bool:
        def printUsedPositions(u: List[bool]):
            print('Used:',end='')
            for c in u:
                if c:
                    print('*',end='')
                else:
                    print('.',end='')
            print()
        def jump(i:int, nums: List[int], usedPositions: List[int]):
            d=True
            if i==len(nums)-1:
                if d: print("Goal reached at position ",i)
                return True
            if i>=len(nums):
                if d: print("Overshoot to position ",i)
                return False
            if usedPositions[i]:
                if d: print ("Occupied position ",i)
                return False
            usedPositions[i] = True
            if d: print ("%i "%i,end='')
            if d: printUsedPositions (usedPositions)
            for j in range(nums[i],0,-1):
                if d: print('%i->'%i,end='')
                if jump(i+j,nums,usedPositions):
                    return True
            return False
        ll=len(nums)
        if ll==1: return True
        usedPositions = [False for i in range(ll)]
        return jump(0, nums, usedPositions)

s=Solution()
try:
    v=list(map(int,sys.argv[1:]))
except:
    printf("Error, bad numbers: ",sys.argv[1:])
print(s.canJump(v))
