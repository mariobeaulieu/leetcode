#!/usr/bin/env python

import sys
from typing import List

class Solution:
    def searchRange(self, nums: List[int], t:int) -> List[int]:
        debug=True
        nb   = len(nums)
        if nb<1: return [-1,-1]
        d0   = (nb+1)//2
        i0   = d0-1
        # imin is the index of the largest value visited smaller than t
        # imax is the index of the smallest value visited larger than t
        imin = 0
        imax = nb-1
        while d0>1:
            if debug: print('Looking for value: i0=%i, d0=%i'%(i0,d0))
            d0 =(d0+1)//2
            if  nums[i0]<t:
                imin=i0
                i0+=d0
                if i0>=nb-1: i0=nb-1
            elif nums[i0]>t:
                imax=i0
                i0-=d0
                if i0<0: i0=0
            else:
                break
        if debug: print('Looking for value: i0=%i, d0=%i'%(i0,d0))
        if nums[i0]!=t:
            if i0>0 and nums[i0-1]==t:
                i0=i0-1
            elif i0<nb-1 and nums[i0+1]==t:
                i0=i0+1
            else:
                return [-1,-1]
        # We found an entry with value t.
        # It could be any t in: q,r,s,t0,t1,t2,t3,t4,t5,u,v
        # Now try to find t0, it's between imin and i0
        if debug: print('Found %i at index %i. Limit indexes are [%i,%i]'%(t,i0,imin,imax))
        if nums[imin]<t:
            n1 = i0-imin+1
            d1 = (n1+1)//2
            i1 = imin + d1 - 1
            while d1>1:
                if debug: print('Looking for min: i1=%i, d1=%i'%(i1,d1))
                d1 = (d1+1)//2
                if  nums[i1]<t:
                    i1+=d1
                    if i1>i0: i1=i0
                elif nums[i1]>=t:
                    i1-=d1
                    if i1<=imin: i1=imin+1
            imin=i1
            if debug: print('Looking for min: i1=%i, d1=%i'%(i1,d1))
        res1=res2=-1
        if nums[imin]==t:
            res1=imin
        elif nums[imin+1]==t:
            res1=imin+1
        if debug: print('Found first value %i at index %i'%(t,res1))
        if res1==-1: return [-1,-1]
        if nums[imax]>t:
            n2 = imax-i0+1
            d2 = (n2+1)//2
            i2 = i0 +d2 - 1
            while d2>1:
                d2 = (d2+1)//2
                if  nums[i2]<=t:
                    i2+=d2
                    if i2>=imax: i2=imax-1
                elif nums[i2]>t:
                    i2-=d2
                    if i2<=i0: i2=i0
            imax=i2
        if nums[imax]==t:
            res2=imax
        elif nums[imax-1]==t:
            res2=imax-1
        return [res1, res2]

try: 
    n=list(map(int, sys.argv[1:-1]))
    t=int(sys.argv[-1])
except:
    print('\nProgram to find the index of first and last given value in a sorted array')
    print('\nUsage: %s <sorted array values> <value to search>'%sys.argv[0])
    print('\nExample:\n  %s 5 7 7 8 8 10 8'%sys.argv[0])
    print('Would search value 8 in sorted array 5 7 7 8 8 10\nIn this case, [3,4] is returned.\n[-1,-1] if value is not found.')
    sys.exit(-1)
s=Solution()
print(s.searchRange(n,t))
    
