#!/usr/bin/env python

import sys
from typing import List

class Solution:
    def binSearch(self, v:int, li:List[int]) -> int:
        lll = ll = len(li)
        i  = ll//2
        while ll>1:
            ll = (ll+1)//2
            if li[i]>v:
                i -= ll
                if i<0: i=0
            elif li[i]<v:
                i += ll
                if i>=lll: i=lll-1
            else:
                return i
        return i
    def threeSum(self,nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums)<3:
            return res
        nums.sort()
        ln=len(nums)
        mi=nums[0]
        ma=nums[-1]
        pvi=mi-1
        for i in range(ln-2):
            vi=nums[i]
            if vi != pvi:
                pvi= vi
                pvj= mi-1
                # Minimum value for vj will be -vi-ma
                minj = self.binSearch(-vi-ma, nums[i+1:-1])+i+1
                #print('searching value %i in list yields minj=%i, list='%(-vi-ma,minj-i-1),nums[i+1:-1])
                for j in range(minj,ln-1):
                    vj=nums[j]
                    if vj != pvj:
                        pvj= vj
                        v  =-vi-vj
                        if mi <= v <= ma :
                            if v in nums[j+1:]:
                                #r = [vi,vj,v]
                                #r.sort()
                                #if r not in res:
                                res.append([vi,vj,v])
        return res

if len(sys.argv) < 4:
    print('Usage: %s <list of integers>\nThe program will return triplets whose sum is 0'%sys.argv[0])
else:
    S=Solution()
    v=list(map(int,sys.argv[1:]))
    #for x in v:
    #    print(S.binSearch(x,v))
    print('List of triplets with sum is 0:\n',S.threeSum(v))
