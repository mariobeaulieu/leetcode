#!/usr/bin/env python

import sys

class Solution:
    def longestValidParentheses(self, s:str) -> int:
        # Convert string in a list
        s=list(s)
        nb=len(s)
        # Discard all ) at the beginning of ss
        i=0
        while i<nb and s[i]==')': i+=1
        nb-=i
        if nb<2: return 0
        s=s[i:]
        o=[]
        for i in range(nb):
            # Scan for ')', setting o to indexes of all '(' found
            if s[i]=='(':
                o.append(i)
            elif s[i]==')':
                if len(o)!=0:
                    s[o.pop()]='1'
                    s[i]='1'
        # Now count the successive '1':
        best=result=0
        for i in range(nb):
            if s[i]=='1':
                result+=1
            else:
                if result>best: best=result
                result=0
        if result>best: best=result
        return best
try:
    s=sys.argv[1]
except:
    print('Usage: %s <bunch of open and close parenthesis>'%sys.argv[0])
    sys.exit(-1)
ss=Solution()
print ('Longest valid parenthesis sequence: %i'%ss.longestValidParentheses(s))
