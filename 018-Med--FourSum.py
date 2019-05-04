#!/usr/bin/env python

import sys
from typing import List

class Solution:
    debug=True
    def binSearch(self, nums:List[int], target: int) -> int:
        d=ll=len(nums)
        i=ll//2
        while d>1:
            d=(d+1)//2
            if   nums[i]<target: i=min(i+1,ll-1)
            elif nums[i]>target: i=max(i-1,0)
            else: break
        # If target value occurs many times, we need to pick the first one
        while i>0    and nums[i]>=target: i-=1
        while i<ll-1 and nums[i]< target: i+=1
        if self.debug: print('Searching target %i returned index %i of array'%(target,i),nums)
        return i
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ll=len(nums)
        if ll<4: return []
        nums.sort()
        res=[]
        mi1=nums[0]-1
        pa =mi1 # just a value different from a
        for ia,a in enumerate(nums[:-3]):
            if a!=pa:
                pa=a
                # If c and d are max values, what is b?
                if self.debug: print('a=%i'%a,end=' ')
                bmin =target-a-nums[-1]-nums[-2]
                ibmin=self.binSearch(nums[ia+1:-2],bmin)+ia+1
                pb   =mi1 #again, just a value different from b
                for ib,b in enumerate(nums[ibmin:-2]):
                    if pb!=b:
                        pb=b
                        # Now if d is the max, what is the value of c?
                        cmin =target-a-b-nums[-1]
                        if self.debug: print('b=%i'%b,end=' ')
                        icmin=self.binSearch(nums[ibmin+ib+1:-1],cmin)+ibmin+ib+1
                        idmax=ll-1
                        while icmin<idmax:
                            if self.debug: print ('ic=%i,id=%i'%(icmin,idmax))
                            r=a+b+nums[icmin]+nums[idmax]
                            if   r<target:
                                icmin+=1
                                while icmin<idmax and nums[icmin-1]==nums[icmin]: icmin+=1
                            elif r>target:
                                idmax-=1
                                while icmin<idmax and nums[idmax+1]==nums[idmax]: idmax-=1
                            else:
                                res.append([a,b,nums[icmin],nums[idmax]])
                                if self.debug: print('Found:',res[-1])
                                icmin+=1
                                idmax-=1
                                while icmin<idmax and nums[icmin]==nums[icmin-1]: icmin+=1
                                while icmin<idmax and nums[idmax]==nums[idmax+1]: idmax-=1
        return res

if len(sys.argv)<6:
    print('Usage: %s <list of at least 4 integers plus target>'%sys.argv[0])
else:
    s=Solution()
    n=list(map(int,sys.argv[1:-1]))
    if s.debug:
        n.sort()
        for i in range(n[0]-3,n[-1]+3):
            print('Search %i: got index %i from array'%(i,s.binSearch(n,i)),n)
    t=int(sys.argv[-1])
    print (s.fourSum(n,t))
