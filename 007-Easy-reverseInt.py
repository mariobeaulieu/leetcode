#!/usr/bin/env python
import sys
class Solution:
    def reverse(self, x: int) -> int:
        limit=2**31
        y=0
        if x<0:
            x=-x
            negative=True
        else:
            negative=False
        while x>0:
            y=10*y+x%10
            x//=10
        if negative:
            y=-y
            if y<=-limit:
               y=0
        else:
            if y>=limit-1:
               y=0
        return y

s=Solution()
x=int(sys.argv[1])
print('%i -> %i'%(x,s.reverse(x)))
