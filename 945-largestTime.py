#!/usr/bin/env python

import sys

from typing import List

def largestTime(A: List[int]) -> str:
        A.sort()
        h = 'x'
        if 2 in A:
            AP = A[:]
            AP.remove(2)
            for i in [3,2,1,0]:
                if i in AP:
                    APP=AP[:]
                    APP.remove(i)
                    if APP[0]<6:
                        A.remove(i)
                        A.remove(2)
                        h = str(20+i)
                        break
        if h=='x' and 1 in A:
            A.remove(1)
            h = str(10+A.pop())
        elif h=='x':
            if 0 in A:
                A.remove(0)
                h = '0'+str(A.pop())
            else:
                return ''
        if A[-1]<6:
            m = str(A.pop())+str(A.pop())
        else:
            if A[0]<6:
                m = str(A[0])+str(A[1])
            else:
                return ''
        return h+':'+m
print ( largestTime([int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])]))

