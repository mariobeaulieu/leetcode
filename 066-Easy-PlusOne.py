#!/usr/bin/env python
import sys
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ll=len(digits)
        for i in range(ll):
            ll2=ll-1-i
            digits[ll2]+=1
            if digits[ll2]<10:
                break
            digits[ll2]=0
            if ll2==0:
               digits.insert(0,1)
        return digits

s = Solution()
myList = list(map(int, sys.argv[1:]))
print('Result of PlusOne of the last item of the list:'%s.plusOne(myList))

