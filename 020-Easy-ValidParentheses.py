#!/usr/bin/env python

import sys

class Solution:
    parentheses=['(',')','[',']','{','}']
    def isValid(self, s: str) -> bool:
        prev=[]
        for c in s:
            if c in self.parentheses:
                i=self.parentheses.index(c)
                if i%2 == 0:
                    # This is an open parenthese, store its index
                    prev.append(i)
                else:
                    # This is a close parenthese, does it
                    # match the last open one?
                    try:
                        if prev.pop()+1 != i:
                            return False
                    except IndexError:
                        return False
        if len(prev) != 0:
            return False
        else:
            return True
if len(sys.argv) != 2:
    print('Usage: %s <string including open and closed parenthesis ({[]}) in any order'%sys.argv[0])
else:
    s=Solution()
    print(s.isValid(sys.argv[1]))
