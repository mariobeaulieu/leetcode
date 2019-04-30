#!/usr/bin/env python

import sys
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0 or len(strs[0])==0:
            return ''
        longest=[]
        for i in range(len(strs[0])):
            letter=strs[0][i]
            result=True
            for w in strs:
                if i>=len(w) or w[i] != letter:
                    result=False
                    break
            if result:
                longest.append(letter)
            else:
                break
        return ''.join(longest)

if len(sys.argv)<2:
    print('Usage: %s <list of words>'%sys.argv[0])
else:
    S=Solution()
    print('Longest prefix is: <%s>'%S.longestCommonPrefix(sys.argv[1:]))
