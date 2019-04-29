#!/usr/bin/env python

import sys
from typing import List

def isRectangleOverlap(rec1: List[int], rec2: List[int]) -> bool:
        if rec1[0]>rec1[2]: rec1[0],rec1[2]=rec1[2],rec1[0]
        if rec1[1]>rec1[3]: rec1[1],rec1[3]=rec1[3],rec1[1]
        if rec2[0]>rec2[2]: rec2[0],rec2[2]=rec2[2],rec2[0]
        if rec2[1]>rec2[3]: rec2[1],rec2[3]=rec2[3],rec2[1]   
        if rec1[2]>rec2[0] and rec1[0]<rec2[2]:
            if rec1[3]>rec2[1] and rec1[1]<rec2[3]: return True
        return False            

p=[]
for i in sys.argv[1:]:
  p.append(int(i))
print(p)
print(isRectangleOverlap(p[0:4],p[4:8]))

