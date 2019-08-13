#!/usr/bin/env python

import sys

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.rstrip()
        ll=len(s)
        if ll==0: return 0
        startWord = s.rfind(' ')
        if startWord == -1:
            return ll
        else:
            return ll-startWord-1
s=Solution()
n = s.lengthOfLastWord(' '.join(sys.argv))
print('Last word has %i characters'%n)

