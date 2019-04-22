#!/usr/bin/env python
import sys

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        global nm,pp,lp1
        def getNewCm(p) -> str:
            global nm,pp,lp1
            nm=1
            if pp<lp1:
                pp+=1
                cm=p[pp]
                if pp<lp1:
                    if p[pp+1]=='*':
                        nm=0
                        pp+=1
                        # Now if the next character is also the same, skip it
                        if pp<lp1:
                            while p[pp+1]==cm:
                                pp+=1
                                if pp==lp1:
                                    break
                #print('Now to match with %s %i times'%(cm,nm))
            else:
                cm=''
            return cm
        match=True
        #Length of strings s and p
        ls = len(s)
        lp1= len(p)-1
        if lp1<0:
            if ls==0:
                return True
            else:
                return False
        #Position in s and in p
        ps = 0
        pp = -1
        nm = 1 # Number of allowed matches
        #cm = character to match (from p)
        cm = getNewCm(p)
        for c in s:
            #print('Character from string: %s. To match with %s %i times'%(c,cm,nm))
            # If we didn't match, but we had 0 or more matches
            while c!=cm and cm!='.' and nm==0:
                # We had a 0 match.
                # Let's get the next character to match from p
                cm = getNewCm(p)
                #print('Now to match with %s %i times'%(cm,nm))
                if cm=='':
                    match=False
            if c==cm or cm=='.':
                #Match valid
                if nm==1:
                    # 1 match was allowed. Get next char from p
                    cm = getNewCm(p)
            else:
                match=False
            if match==False:
                break
        # If there are extra chars to match in p that were not, then we fail
        #print('Exited match loop. cm=%s, pp=%i'%(cm,pp))
        if cm!='' and nm!=0:
            match=False
        # Now check if there are more chars that we need to match from p
        while cm!='' and nm==0 and match==True:
            # See if more chars need to be matched from p
            cm = getNewCm(p)
            if cm!='' and nm==1:
                #We now have character cm with 1 required match that doesn't match with s
                match=False
        return match

if len(sys.argv) != 3:
    print("Usage: %s <stringToMatch> <patternWith.and*>"%sys.argv[0])
else:
    S=Solution()
    print(S.isMatch(sys.argv[1],sys.argv[2]))
