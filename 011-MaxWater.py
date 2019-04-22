#!/usr/bin/env python

import sys
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        numv=len(height)
        maxi=i=0
        maxj=j=numv-1
        hi  =height[i]
        hj  =height[j]
        maxarea=min(hi,hj)*j
        while i+1<j:
            #print('i=%i,j=%i,hi=%i,hj=%i'%(i,j,hi,hj))
            if hi<hj:
                i+=1
                while height[i]<=hi and i<j:
                    i+=1
                hi=height[i]
            else:
                j-=1
                while height[j]<=hj and i<j:
                    j-=1
                hj=height[j]
            a=min(hi,hj)*(j-i)
            if a>maxarea:
                maxarea = a
                maxi=i
                maxj=j
        return maxarea

if len(sys.argv)<3:
    print('Usage: %s <list of at least 2 integers>'%sys.argv[0])
else:
    S=Solution()
    heights=[]
    for v in sys.argv[1:]:
        heights.append(int(v))
    print (S.maxArea(heights))
