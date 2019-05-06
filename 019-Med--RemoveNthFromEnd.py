#!/usr/bin/env python

import sys
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def printIt(self):
        if self.next == None:
            print(self.val)
        else:
            print('%i -> '%self.val,end='')
            self.next.printIt()
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ptrs=[head]
        count = 0
        while ptrs[-1] != None:
            ptrs.append(ptrs[-1].next)
            count += 1
        # Last ptrs is None, remove it
        ptrs.pop()
        if len(ptrs) == 0:
            return None
        # Now remove node count-n
        if count == n: # This is node 0: return list from second node
            print('Removing first element')
            return head.next
        if n == 1: # This is the last node
            print('Removing last element')
            ptrs[-2].next = None
        else:
            print('Count=%i, removing %i by pointing element %i to element %i'%(count,ptrs[-n].val,ptrs[-n-1].val,ptrs[-n+1].val))
            ptrs[-n-1].next = ptrs[-n+1]
        return ptrs[0]

if len(sys.argv)<3:
    print('Usage: %s <list of integers followed by index from end to remove>'%sys.argv[0])
    print('  Ex: %s 1 2 3 4 5 4'%sys.argv[0])
    print('      To create linked list of values 1 2 3 4 5\n      and then remove the 4th one from last (value 2)')
else:
    v=list(map(int,sys.argv[1:-1]))
    n=int(sys.argv[-1])
    h=head=ListNode(v[0])
    for p in v[1:]:
        h.next=ListNode(p)
        h=h.next
    head.printIt()
    s=Solution()
    s.removeNthFromEnd(head,n).printIt()
