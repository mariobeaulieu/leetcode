#!/usr/bin/env python

import sys
import random
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def calcMedian(nums:List[int],i0:int,i1:int) -> float:
            #print('calculating median between values %i and %i'%(nums[i0],nums[i1])) 
            if (i0 + i1)%2 == 1:
                # median is between 2 indices
                i=int((i0 + i1 - 1)/2)
                median = (nums[i]+nums[i+1])/2
            else:
                # median falls on 1 value
                median = float(nums[int((i0 + i1)/2)])
            return median

        n1   = len(nums1)
        n2   = len(nums2)
        ini1 = ini2=0
        end1 = n1-1
        end2 = n2-1
        if n1==0: return calcMedian(nums2,ini2,end2)
        if n2==0: return calcMedian(nums1,ini1,end1)
        vmin1= nums1[0]
        vmin2= nums2[0]
        vmax1= nums1[end1]
        vmax2= nums2[end2]
        maxValue=max(vmax1,vmax2)
        done1= done2= False
        while True:
            if vmin1<vmin2:
                #print('removing from list1 %i'%nums1[ini1],end='')
                ini1+=1
                if ini1>end1:
                    done1 = True
                    # I need to consume 1 value from the end, and nums1 is empty
                    #print(' and from list2 %i (list1 empty)'%nums2[end2])
                    end2 -= 1
                    break
                else:
                    vmin1 = nums1[ini1]
            else:
                #print('removing from list2 %i'%nums2[ini2],end='')
                ini2+=1
                if ini2>end2:
                    done2 = True
                    # I need to consume 1 value from the end, and nums2 is empty
                    #print(' and from list1 %i (list2 empty)'%nums1[end1])
                    end1 -= 1
                    break
                else:
                    vmin2 = nums2[ini2]
            if vmax1>vmax2:
                #print(' and from list1 %i'%nums1[end1])
                end1-=1
                if end1<ini1:
                    done1 = True
                    break
                else:
                    vmax1 = nums1[end1]
            else:
                #print(' and from list2 %i'%nums2[end2])
                end2-=1
                if end2<ini2:
                    done2 = True
                    break
                else:
                    vmax2 = nums2[end2]
        if done1:
            # If nums2 is also finished, the median is between min1 and max2
            if end2<ini2:
                return (vmin1+vmax2)/2
            else:
                # The median is at the middle of nums2
                return calcMedian(nums2,ini2,end2)
        else:
            # If nums1 is also finished, the median is between min1 and max2
            if end1<ini1:
                return (vmin2+vmax1)/2
            else:
                return calcMedian(nums1,ini1,end1)

def genList(n:int) -> List[int]:
    s=[]
    for i in range(n):
        s.append(random.randint(1,20))
    s.sort()
    return s

if len(sys.argv)<3:
    print('Usage: %s <numValuesFirstList> <numValuesSecondList>'%sys.argv[0])
else:
    n1=int(sys.argv[1])
    n2=int(sys.argv[2])
    l1=genList(n1)
    print(l1)
    l2=genList(n2)
    print(l2)
    s=Solution()
    v = s.findMedianSortedArrays(l1,l2)
    print(v)

