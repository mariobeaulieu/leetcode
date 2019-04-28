#!/usr/bin/env python
import sys
import subprocess
import os

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #print ('\n6-Starting match with s=%s, p=%s'%(s,p))
        global nm,pp,cmstar
        def getNewCm(p) -> str:
            global nm,pp,cmstar
            nm=1
            lp1=len(p)-1
            if pp<lp1:
                pp+=1
                cm=p[pp]
                if pp<lp1:
                    if p[pp+1]=='*':
                        nm=0
                        #print('Star match. pp=%i, p='%pp,p)
                        # If we have 2 redundant x*, jump to the second pair
                        while pp+2<lp1 and p[pp+3]=='*' and (cm==p[pp+2] or (cm=='.' or p[pp+2]=='.')):
                            if p[pp+2]=='.':
                                cm='.'
                            pp+=2
                            #print('Consumed %s*. Now, pp%i, p=='%(p[pp-2],pp),p)
                        pp+=1
                        # Now if the next character is also the same, use it instead
                        if pp<lp1 and p[pp+1]==cm and cm!='.':
                            if not (pp+1<lp1 and p[pp+2]=='*') :
                                # Flip the * with the value of cm we just found
                                p[pp],p[pp+1]=cm,'*'
                                pp-=1
                                nm=1
                        else:
                            cmstar.append(cm)
            else:
                cm=''
            return cm
        match=True
        cmstar =[] # Characters that were consumed by a star
        #Length of strings s and p
        ls = len(s)-1
        lp1= len(p)-1
        if lp1<0:
            if ls<0:
                return True
            else:
                return False
        # Convert p as a list to be able to manipulate it
        p=list(p)
        #Position in s and in p
        ps = 0
        pp = -1
        nm = 1 # Number of allowed matches
        #cm = character to match (from p)
        cm = getNewCm(p)
        while ps<=ls:
            #print('52-s=%s, p=%s, cm=%s, nm=%i'%(s[ps:],''.join(p[pp:]),cm,nm))
            if nm==0:
                # In this case, we will try recursively from this position pp points
                # to the star. Replace the * with the character we are looking for
                match=False
                p[pp] = cm
                tnm,tpp = nm,pp
                tcmstar=cmstar[:]
                for pps in range(ps,ls+1):
                    if cm!='.' and s[pps]!=cm:
                        break
                    nm,pp = tnm,tpp
                    cmstar= tcmstar[:]
                   #print('64-pp=%i, ps=%i, p='%(pp,ps),p)
                    match = self.isMatch(s[pps:],''.join(p[pp:]))
                    if match: break
                if not match:
                    # Try if .* matches 0 characters
                    nm,pp = tnm,tpp
                    cmstar= tcmstar[:]
                   #print('71-"." matches 0-char: pp=%i, ps=%i, lp1=%i, p='%(pp,ps,lp1),p)
                    if pp<lp1:
                       #print('73-"." matches 0-char: pp=%i, ps=%i, p='%(pp+1,ps),p)
                        match = self.isMatch(s[ps:],''.join(p[pp+1:]))
                return match
            else:
                c=s[ps]
                #print('78-Character from string: %s. To match with %s %i times'%(c,cm,nm))
                # If we didn't match, but we had a *
                while c!=cm and cm!='.' and nm==0:
                    # Let's get the next character to match from p
                    cm = getNewCm(p)
                   #print('83-Now to match with %s %i times'%(cm,nm))
                    #if cm=='':
                    #    match=False
                if c==cm or cm=='.':
                    #Match valid
                    if nm==1:
                        # 1 match was allowed. Reset cmstar and get next char from p
                        cmstar = []
                       #print('91-Match 1 value %s with <%s>. cmstar needs to be emptied'%(c,cm))
                        cm = getNewCm(p)
                    else:
                        #Valid match with *. All other cmstar are invalidated
                        cmstar = [cm]
                       #print('96-Match %s with a *. All other cmstar are invalidated. New cmstar is',cmstar)
                else:
                    good=False
                    # Check if we match something from cm*
                    #print('96-Mismatch. cmstar=',cmstar)
                    for cm in cmstar:
                        if c==cm or cm=='.':
                            #We had something like a*b*c*b and need to match abb (no c)
                            #cmstar would contain [a,b,c] but after this only [b]
                            cmstar = [cm]
                            nm=0
                            good=True
                            break
                    if good==False:
                       #print('110-Not good, so exiting with false')
                        return False
            ps+=1
        # If there are extra chars to match in p that were not, then we fail
        # Unless those chars are covered in cmstar
        while cm!='':
            #print('116-In loop while cm!="" (cm=<%s>), nm=%i, cmstar='%(cm,nm),cmstar)
            # Skip all characters followed with *
            while cm!='' and nm==0:
                cm = getNewCm(p)
                #print('120-Got new cm=%s,nm=%i'%(cm,nm))
            if cm!='' and nm!=0:
                #print('122-return false, cm=<%s>, nm=%i, cmstar='%(cm,nm),cmstar)
                return False
            #if cm in cmstar:
            #    print('121-The char to match was in cmstar. Reset cmstar to only this char.')
            #    cmstar=[cm]
            #    cm = getNewCm(p)
        return match

if len(sys.argv) != 3:
    print("Usage: %s <stringToMatch> <patternWith.and*>"%sys.argv[0])
else:
    S=Solution()
    r=S.isMatch(sys.argv[1],sys.argv[2])
    print(r)
    cmd = 'echo %s | grep -w "%s"'%(sys.argv[1],sys.argv[2])
    print(cmd)
    output = os.system(cmd)
    if output == 0:
        print('There is a match')
        if r:
            print('\n***** Success. *****')
        else:
            print('\n***** ERROR *****')
    else:
        print('No match')
        if not r:
            print('\n***** Success. *****')
        else:
            print('\n***** ERROR *****')
