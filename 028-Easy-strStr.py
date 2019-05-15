#!/usr/bin/env python

import sys

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lh=len(haystack)
        ln=len(needle)
        if ln==0: return 0
        if ln>lh: return -1
        n=needle[0]
        for h,c in enumerate(haystack[:lh-ln+1]):
            if c==n:
                i=0
                while haystack[h+i]==needle[i]:
                    i+=1
                    if i==ln: return h
        return -1
try:
    hay=sys.argv[1]
    needle=sys.argv[2]
except:
    print('Find the first occurrence of needle in haystack')
    print('Usage: %s <string (the haystack)> <string(the needle)>'%sys.argv[0])
    sys.exit(-1)
s=Solution()
print(s.strStr(hay,needle))
