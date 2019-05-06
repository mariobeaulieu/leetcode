#!/usr/bin/env python

import  sys
from typing import  List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==0: return []
        myList=['(']
        nbOpCl=[[1,0]]
        allClosed=False
        while not allClosed:
            # Double the list, adding '(' to 1st item and ')' to last one
            myList2=[]
            nbOpCl2=[]
            allClosed=True
            for i in range(len(myList)):
                nbOp=nbOpCl[i][0]
                nbCl=nbOpCl[i][1]
                if nbOp<n:
                    myList2.append(myList[i]+'(')
                    nbOpCl2.append([nbOp+1,nbCl])
                if nbCl<nbOp:
                    myList2.append(myList[i]+')')
                    nbOpCl2.append([nbOp,nbCl+1])
                    if nbCl+1<n: allClosed=False
            myList=myList2
            nbOpCl=nbOpCl2
            print('myList is now: ',myList)
            print('nbOpCl is now: ',nbOpCl)
        return myList

s=Solution()
try:
    n=int(sys.argv[1])
    print('Here are the combinations of %i parenthesis:')
    print(s.generateParenthesis(n))
except IndexError:
    print('Usage: %s <int>\n    You must provide a value for the number of parenthesis to print'%sys.argv[0])
except ValueError:
    print('Usage: %s <int>\n    The value provided: <%s> is not a number'%(sys.argv[0],sys.argv[1]))
