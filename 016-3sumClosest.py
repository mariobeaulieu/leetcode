#!/usr/bin/env python

# 3-Sum closest:  return the 3 numbers from a list whose sum is closest to a given target

import sys
from typing import List

class Solution:
    def binSearchLess(self, n:List[int], t:int) -> int:
        # Return the index of the first value of the array less than t
        ll=d=len(n)
        ll-=1
        i=d//2
        while d>1:
            d=(d+1)//2
            if   t<n[i]: i=max( 0,i-(d+1)//2)
            elif n[i]<t: i=min(ll,i+(d+1)//2)
            else:break
        # n may be -1 0 1 1 2... with t=1, i may be 3. We want i=1
        while n[i]>=t and i>0: i-=1
        return i
    def threeSumClosest(self, nums:List[int], target:int) -> int:
        # Sort the array
        nums.sort()
        ll=len(nums)-1
        ma=nums[-1]
        s =nums[0]+nums[1]+nums[2]
        ds=abs(s-target)
        for ia,a in enumerate(nums[0:-2]):
            # a+b+c=target
            # If c==ma, then b=target-ma-a
            # That's the minimum possible for b
            minb=self.binSearchLess(nums[ia+1:ll],target-ma-a)
            ib=minb+ia+1
            ic=ll
            while ib<ic:
                s2 =a+nums[ib]+nums[ic]
                ds2=abs(s2-target)
                if ds2<ds: s,ds=s2,ds2
                if   s2>target: ic-=1 #ic should be decreased to reduce s2
                elif s2<target: ib+=1 #increase ib to augment s2
                else:#we need to check both decrease ic and increase ib
                    if ib+1==ic: break
                    s2 =a+nums[ib+1]+nums[ic]
                    ds2=abs(s2-target)
                    if ds2<ds: s,ds=s2,ds2
                    ic-=1
        return s

if len(sys.argv)<4:
    print('Usage: %s <list of integers>\nThe last value is the target for the sum of 3 values.\nOutput is the closest sum found'%sys.argv[0])
else:
    S=Solution()
    n=list(map(int,sys.argv[1:-1]))
    t=int(sys.argv[-1])
    print('Closest sum is ',S.threeSumClosest(n,t))



