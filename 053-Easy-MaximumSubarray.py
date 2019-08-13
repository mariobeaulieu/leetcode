#!/usr/bin/env python
import sys
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currMax = maxMax = nums[0]
        for i in range(1,len(nums)):
            # The list may contain only negative numbers
            # In this case, the greatest of these is the answer
            if maxMax < 0 and nums[i] < 0:
                if nums[i] > maxMax:
                    maxMax = nums[i]
            else:
                if currMax < 0: currMax = 0
                currMax += nums[i]
                if currMax > maxMax:
                    maxMax = currMax
        return maxMax

s = Solution()
myList = list(map(int, sys.argv[1:]))
print('Largest consecutive sum is %i'%s.maxSubArray(myList))

