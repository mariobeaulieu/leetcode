#!/usr/bin/env python

import sys

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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1==None: return l2
        if l2==None: return l1
        if l1.val<l2.val:
            l3=l4=ListNode(l1.val)
            l1=l1.next
        else:
            l3=l4=ListNode(l2.val)
            l2=l2.next
        while l1!=None and l2!=None:
            if l1.val<l2.val:
                l4.next = l1
                l1=l1.next
            else:
                l4.next = l2
                l2=l2.next
            l4=l4.next
        #For the rest of the list
        if l1!=None:
            l4.next=l1
        else:
            l4.next=l2
        return l3
if len(sys.argv)<3:
    print ('Usage: %s <m> <a1 a2 a3... am> <n> <b1 b2 b3... bn>'%sys.argv[0])
    print ('       where all list values are evaluated as strings')
else:
    m=int(sys.argv[1])
    n=int(sys.argv[m+2])
    print('First list: ',end='')
    if m==0:
        l1=None
        print('EMPTY')
    else:
        ll=l1=ListNode(sys.argv[2])
        for i in sys.argv[3:m+2]:
            ll.next=ListNode(i)
            ll=ll.next
        l1.printIt()
    print('Second list:',end='')
    if n==0:
        l2=None
        print('EMPTY')
    else:
        ll=l2=ListNode(sys.argv[3+m])
        for i in sys.argv[4+m:]:
            ll.next=ListNode(i)
            ll=ll.next
        l2.printIt()
    print('Merged list:',end='')
    s=Solution()
    l3=s.mergeTwoLists(l1,l2)
    if l3==None:
        print('EMPTY')
    else:
        l3.printIt()
