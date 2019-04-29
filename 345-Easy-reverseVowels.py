#!/usr/bin/env python
import sys

def reverseVowels(s: str) -> str:
        i0 = 0
        i1 = 1
        s1 = len(s) - 1
        ss = list(s)
        found = s1>0
        while found and i0+i1<=s1:
            while ss[i0] not in 'aeiouAEIOU':
                i0 += 1
                if i0 == s1:
                    found = False
                    break
            if found:
                while ss[-i1] not in 'aeiouAEIOU':
                    i1 += 1
                    if i0+i1 > s1:
                        found = False
                        break
            if found:
                ss[i0],ss[-i1] = ss[-i1],ss[i0]
                i0 += 1
                i1 += 1
        return ''.join(ss)
print( reverseVowels(sys.argv[1]) )
