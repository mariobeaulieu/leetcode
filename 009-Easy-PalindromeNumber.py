#!/usr/bin/env python

import sys

class Solution:
    def isPalindrome(self, x:int) -> bool:
        if x<0: return False
        result = True
        x0=x
        y=0
        while x>0:
            y=y*10+x%10
            x//=10
        return y==x0

if len(sys.argv) != 2:
    print('Usage: %s <integerValueThatIsOrNotAPalindrome>'%sys.argv[0])
else:
    S=Solution()
    x=int(sys.argv[1])
    print(S.isPalindrome(x))
