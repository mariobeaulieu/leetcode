#!/usr/bin/env python
import sys

def romanToInt(s: str) -> int:
        roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        prevV  = 0
        value  = 0
        for i in range(1,len(s)+1):
            v = roman[s[-i]]
            if prevV > v :
                value -= v
            else:
                value += v
            prevV = v
        return value

print (romanToInt(sys.argv[1]))
