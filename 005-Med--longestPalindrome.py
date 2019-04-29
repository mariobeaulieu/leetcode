#!/usr/bin/env python
import sys

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def findPalindrome(i:int, j:int, s:str) -> int:
            # this function will return the pos of starting of a palindrome
            # whose middle is at [i] and [j] where j==i or i+1
            while True:
                print('Starting at %i,%i:'%(i,j),end='')
                i-=1
                j+=1
                if i<0 or j>=lon: break
                # We didn't reach any end of the string
                if s[i] != s[j]:  break
            print('Found palindrome %s'%s[i+1:j])
            return i+1

        # I will start at the middle of the palindrome and walk on both sides
        bestLen = 1
        bestStrt= 0
        lon     = len(s)
        if lon<2:
            return s
        for pos in range(lon-1):
            print('p=%i,'%pos,end='')
            i=j=pos
            # Try with pos at the middle
            newStrt=findPalindrome(pos,pos,s)
            newLen =(pos-newStrt)*2+1
            if newLen>bestLen:
                bestLen = newLen
                bestStrt= newStrt
            # Now try if the middle of palindrome is between pos and pos+1
            if s[pos]==s[pos+1]:
                newStrt=findPalindrome(pos,pos+1,s)
                newLen =(pos-newStrt+1)*2
                if newLen>bestLen:
                    bestLen = newLen
                    bestStrt= newStrt
        return s[bestStrt:bestStrt+bestLen]

if len(sys.argv) != 2:
    print('Usage: %s <string>'%sys.argv[1])
else:
    g=Solution()
    print(g.longestPalindrome(sys.argv[1]))
