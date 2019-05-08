#!/usr/bin/env python

import sys
from typing import List

class ListNode:
    def __init__(self,x):
        self.val =x
        self.next=None
    def printIt(self):
        if self.next == None:
            print(self.val)
        else:
            print(self.val,end='->')
            self.next.printIt()
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nonEmpty=[]
        vals=[]
        for l in lists:
            if l != None:
                nonEmpty.append(l)
                vals.append(l.val)
        ll=len(nonEmpty)
        if ll==0: return None
        if ll==1: return nonEmpty[0]
        myList1=myList=None
        while len(nonEmpty)>1:
            # Find the list with smallest value
            m=min(vals)
            i=vals.index(m)
            if myList==None:
                myList1=myList=nonEmpty[i]
            else:
                myList.next=nonEmpty[i]
                myList=myList.next
            #Consume that element from my non-empty list then check if it's empty now
            nonEmpty[i]=nonEmpty[i].next
            if nonEmpty[i]==None:
                nonEmpty.pop(i)
                vals.pop(i)
            else:
                vals[i]=nonEmpty[i].val
        #For the rest of the list
        myList.next=nonEmpty[0]
        return myList1
if len(sys.argv)<3:
    print ('Usage: %s <k> <m> <a1 a2 a3... am> <n> <b1 b2 b3... bn>'%sys.argv[0])
    print ('       where k is the number of lists present')
    print ('             m is the length of first list')
    print ('             n is the length of second list')
    print ('               etc.')
    print ('       Note: all list values are evaluated as integers')
else:
    k=int(sys.argv[1])
    j=2
    myList=[]
    for i in range(k):
        n=int(sys.argv[j])
        print('List %i, %i values: '%(i+1,n),end='')
        j+=1
        p=ptr1=None
        if n==0:
            print('EMPTY')
        else:
            p=ptr1=ListNode(int(sys.argv[j]))
            j+=1
            for x in range(n-1):
                p.next=ListNode(int(sys.argv[j]))
                p=p.next
                j+=1
            ptr1.printIt()
        myList.append(ptr1)
    print('Merged list:',end='')
    s=Solution()
    l3=s.mergeKLists(myList)
    if l3==None:
        print('EMPTY')
    else:
        l3.printIt()
