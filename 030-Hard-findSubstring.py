#!/usr/bin/env python

import sys
from typing import List

class Solution:
    # This function checks only if current position is valid
    def checkHere(self, s:str, nbWords: int, unique: List[str], count: List[int]) -> bool:
        nbUnique=len(unique)
        # List of words index to look for
        myList=[i for i in range(nbUnique)]
        myCount=count.copy()
        # Length of these words, all assumed to be same length
        lw=len(unique[0])
        #Character index currently analyzed
        c=0
        while len(myList)>0:
            # List of words currently matching
            active=myList.copy()
            for w in range(lw):
                aa=active.copy()
                for a in aa:
                    if unique[a][w]!=s[c+w]:
                        active.remove(a)
                        if len(active) == 0:
                            return False
            # If the active list isn't empty, we found a word.
            # Remove it from the list
            i=myList.index(active[0])
            myCount[i]-=1
            if myCount[i]==0:
                myCount.pop(i)
                myList.pop(i)
            c+=lw
        # Exiting that loop means all words were found
        return True
    # This function will scan for every starting position in the string s
    def findSubstring(self, s:str, words: List[str]) -> List[int]:
        nbWords=len(words)
        if nbWords==0: return []
        lenStr =len(s)
        lenWord=len(words[0])
        lenAllWords=lenWord*nbWords
        matches=[]
        # Combine words in 2 lists: unique and count
        words.sort()
        count=[1]
        unique=[words[0]]
        n=0
        for w in words[1:]:
            if w==unique[n]:
                count[n]+=1
            else:
                unique.append(w)
                n+=1
                count.append(1)
        for i in range(lenStr-lenAllWords+1):
            if self.checkHere(s[i:],nbWords,unique,count):
                matches.append(i)
        return matches

try:
    s=sys.argv[1]
    w=sys.argv[2:]
except:
    print('Program to find indexes in first string where all words from')
    print('the list following are concatenated. \nEx: ');
    print('  %s barfootthefoobarman foo bar'%sys.argv[0])
    print('Would return [0,9] because barfoo (at index 0) and foobar (at index 9).')
    print('Note: all words in the list are the same length')
    sys.exit(1)
sol=Solution()
print(sol.findSubstring(s,w))
