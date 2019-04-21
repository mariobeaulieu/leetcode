#!/usr/bin/env python
import sys

class Solution:
    def myAtoi(self, s: str) -> int:
        N    = '0123456789'
        MAX  = 2**31-1
        s    = s.strip()
        v    = 0
        valid= False
        sign = 1
        if s=='': return 0
        if s[0]=='-':
            sign = -1
            s    = s[1:]
        elif s[0]=='+':
            s    = s[1:]
        for c in s:
            n    = N.find(c)
            if n<0: break
            v    = 10*v+n
        v = sign*v
        if v<-MAX or v>=MAX: return 0
        return v

if len(sys.argv) != 2:
    print('Usage: %s <integer value>'%sys.argv[0])
else:
    S=Solution()
    print(S.myAtoi(sys.argv[1]))
