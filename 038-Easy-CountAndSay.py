#!/usr/bin/env python

import sys

class Solution:
    def countAndSay(self, n: int) -> str:
        def sayIt(n:int, say:str) -> str:
            if n==1: return say
            say2=[]
            count=1
            ls=len(say)
            for i in range(ls):
                if i==ls-1 or say[i]!=say[i+1]:
                    say2.append(repr(count))
                    say2.append(say[i])
                    count=1
                else:
                    count+=1
            return sayIt(n-1, ''.join(say2))
        return sayIt(n, '1')

try:
    value =int(sys.argv[-1])
except:
    print('Program to generate the suite "count-and-say" starting with value "1"')
    print('Usage:\n%s <number of iterations>'%sys.argv[0])
    print('This suite is:\n1 - "1"\n2 - "11"\n3 - "21"\n4 - "1211"\n5 - "111221"\n...')
    sys.exit(1)
print ('Value is %i'%value)
S=Solution()
for i in range(1,value+1):
    print('%i: %s'%(i,S.countAndSay(i)))
