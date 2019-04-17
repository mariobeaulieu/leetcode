#!/usr/bin/env python
import sys

def reverse2(s:str, k:int) -> str:
        ss=list(s)
        le=len(ss)
        for i0 in range(0,le,2*k):
            i1 = i0+k-1
            if i1 >= le:
                i1=le-1
            print ('i0=%i, i1=%i, string=%s'%(i0,i1,s[i0:i1+1]))
            for j in range(int((i1-i0+1)/2)):
                ss[i0+j],ss[i1-j] = ss[i1-j],ss[i0+j]
        return ''.join(ss)

print (reverse2(sys.argv[1],int(sys.argv[2])))

