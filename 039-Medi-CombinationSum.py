#!/usr/bin/env python

import sys
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def findSum(i0: int, myList: List[int], t: int) -> List[List[int]]):
            result = []
            ll=len(myList)
            if i0==ll: return result
            v =myList[i0]
            nb=t//v
            for i in range(nb):
                t2 = t-v
                if t2<0: return result
                result.append([v])
                if t2==0:
                    return result
                else:
                    findSum(i0+1, myList, 
        # Remove duplicates
        myList = list(set(candidates)).sort()
        ll = len(myList)
        if ll==0: return []
        if myList[0] == 0:
            myList=myList[1:]
            ll-=1
            if ll==0: return []
        return findSum(0, myList, target)

s=Solution()
try:
    v=list(map(int,sys.argv[1:]))
except:
    print ('Error when converting parameters as integers: ', sys.argv[1:])
t=v[-1]
v=v[:-1]
print('Target=%i'%t)
print('Values=',v)
print ('Solution: ',combinationSum(v[:-1],v[-1]))
