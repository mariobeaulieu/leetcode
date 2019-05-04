#!/usr/bin/env python

import sys
from typing import List

class Solution:
    dial={'0':'','1':'','2':'abc','3':'def','4':'ghi','5':'jkl',
          '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)<1: return []
        d=digits[0]
        if len(digits)==1:
            return list(self.dial[d])
        r=self.letterCombinations(digits[1:])
        r2=[]
        for c in self.dial[d]:
            for s in r:
                r2.append(c+s)
        return r2

if len(sys.argv)!=2:
    print('Usage: %s <many digits number with no 0 or 1>'%sys.argv[0])
else:
    s=Solution()
    print(s.letterCombinations(sys.argv[1]))
