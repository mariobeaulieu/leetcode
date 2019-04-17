#!/usr/bin/env python

def convert(s: str, numRows: int) -> str:
    if numRows < 2:
       return s
    else:
        myOutput = ''
        for r in range(numRows):
            i=r
            myOutput += ' '
            while i < len(s):
                myOutput += s[i]
                if r>0 and r<numRows-1:
                    j = i+2*(numRows-r-1)
                    if j<len(s):
                        myOutput += s[j]
                i += 2*(numRows - 1)
        return myOutput

print ( convert('A',1) )
print ( convert('012345678901234567890123456789',2) )


