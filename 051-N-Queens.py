#!/usr/bin/env python

import sys
from typing import List

def solveNQueens(n: int) -> List[List[str]]:
        solutions = []
        queens    = []
        placeQueen(n, queens, solutions)
        return solutions

def placeQueen(n:int, queens:List[int], solutions:List[List[str]]):
        nq = len(queens)
        if nq == n:
            sol=[]
            for i in range(n):
                sol.append('.'*queens[i]+'Q'+'.'*(n-queens[i]-1))
            solutions.append(sol)
            #print(sol)
        else:
            for i in range(n):
                # Check if there is another queen in same column
                valid=True
                for j in range(nq):
                    if queens[j] == i:
                        valid=False
                        break
                if valid:
                    # Check for a queen in left diagonal
                    for j in range(1,min(i,nq)+1):
                       if queens[nq-j]==i-j:
                           valid=False
                           break
                if valid:
                    # Check for a queen in right diagonal
                    for j in range(1,min(n-i-1,nq)+1):
                       if queens[nq-j]==i+j:
                           valid=False
                           break
                if valid:
                    queens.append(i)
                    placeQueen(n,queens,solutions)
                    queens.pop()

n = int(sys.argv[1])
s = solveNQueens(n)
print ('There are %s solutions'%len(s))
cols = 8

for i in range(0, len(s), cols):
   for m in range(n):
      for k in range(i,min(i+cols,len(s))):
         print ('%s  '%s[k][m],end='')
      print()
   print()

