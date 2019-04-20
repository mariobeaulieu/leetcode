#!/usr/bin/env python
import sys
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lon = len(nums)
        for i in range(lon-1):
            for j in range(i+1,lon):
                if nums[i]+nums[j]==target: return [i,j]

s=Solution()
l=len(sys.argv)
nums=[]
for i in sys.argv[1:]:
  nums.append(int(i))
target=nums.pop()

indices = s.twoSum(nums,target)
print(indices)
