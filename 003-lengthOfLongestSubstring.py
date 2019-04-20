#!/usr/bin/env python

import sys

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def findLongest(s):
            index = lon = len(s)
            for i in range(lon-1):
                if i>=index: break
                newIndex = s.find(s[i],i+1)
                if newIndex!=-1 and newIndex<index:
                    index=newIndex
                print('Testing %s with %s, found %i (%i for this string)'%(s,s[i],newIndex,index))
            print()
            return index
        le=len(s)
        if le<2: return le
        longest=0
        for start in range(le-1):
            newLe=findLongest(s[start:])
            if newLe>longest: longest=newLe
        return longest

s=Solution()
print('%s: %i'%(sys.argv[1],s.lengthOfLongestSubstring(sys.argv[1])))

