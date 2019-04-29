#!/usr/bin/env python

import sys
from typing import List

def partitionLabels(S: str) -> List[int]:
        p=[]
        def findPartition(S: str) -> int:
            partLen= 0
            index  = 0
            while True:
                newLen = S.rfind(S[index])
                print ('Searching for %s in string %s, index is %i, found length %i'%(S[index],S,index,newLen))
                if newLen>partLen: partLen = newLen
                index += 1
                if index>partLen:
                    return partLen+1
        ptr=0
        while ptr < len(S):
            newPtr = findPartition(S[ptr:])
            print ( 'S=%s, Starting at index %i, length found is %i'%(S,ptr,newPtr))
            p.append(newPtr)
            ptr+=newPtr
        return p

print( partitionLabels(sys.argv[1]) )
