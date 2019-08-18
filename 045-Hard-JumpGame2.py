#!/usr/bin/env python

import sys
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        def jumpStep(pos: int, nums: List[int]):
            d=True
            ll = len(nums)-1
            if pos==ll: return 0
            maxStep= 0
            newPos = pos
            for i in range(1,nums[pos]+1):
                p = pos+i
                if p >= ll: return 1
                if i+nums[p] > maxStep:
                    newPos = p
                    maxStep=i+nums[p]
            if maxStep == 0: return -1
            if d: print('From value %i at pos %i, jump to value %i at pos %i'%(nums[pos], pos, nums[newPos], newPos))
            value = jumpStep(newPos, nums)
            if value>0:
                return value+1
            else:
                return value
        return jumpStep(0, nums)

s=Solution()
try:
    v=list(map(int, sys.argv[1:]))
except:
    print('Error when converting parameters to a list of integers: ',sys.argv[1:])

print(s.jump(v))
