#!/usr/bin/env python

import sys
from typing import List

class Solution:
    def binSearch(self, v:int, li:List[int]) -> int:
        lll = ll = len(li)
        if ll<2: return 0
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
                break 
        while i>0 and li[i-1]==li[i]:
            i-=1
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
                # Minimum value for vj will be -vi-ma
                minj = self.binSearch(-vi-ma, nums[i+1:-1])+i+1
                #print('searching value %i in list yields minj=%i, list='%(-vi-ma,minj-i-1),nums[i+1:-1])
                j=minj
                vj=nums[j]
                k=ln-1
                vk=nums[k]
                while j<k:
                    v=vi+vj+vk
                    #print('(i,j,k)=(%i,%i,%i) -> (vi,vj,vk)=(%i,%i,%i) -> Sum = %i'%(i,j,k,vi,vj,vk,v))
                    if v<0:
                        pvj=vj
                        while pvj==vj:
                            j+=1
                            if j>=ln: break
                            vj=nums[j]
                    elif v>0:
                        pvk= vk
                        while pvk==vk:
                            k-=1
                            if k<=1: break
                            vk=nums[k]
                    else:
                        res.append([vi,vj,vk])
                        pvj=vj
                        while pvj==vj:
                            j+=1
                            if j>=ln: break
                            vj=nums[j]
                        pvk= vk
                        while pvk==vk:
                            k-=1
                            if k<=1: break
                            vk=nums[k]
        return res

if len(sys.argv) < 4:
    print('Usage: %s <list of integers>\nThe program will return triplets whose sum is 0'%sys.argv[0])
else:
    S=Solution()
    v=list(map(int,sys.argv[1:]))
    #for x in range(v[0],v[-1]):
    #    print('%i --> %i'%(x,S.binSearch(x,v)))
    print('List of triplets with sum is 0:\n',S.threeSum(v))
