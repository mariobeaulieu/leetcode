#!/usr/bin/env python

import sys

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        v=l1.val+l2.val
        l3=l4=ListNode(v%10)
        v0=int(v/10)
        l1=l1.next
        l2=l2.next
        while l1!=None or l2!=None or v0!=0:
            va=vb=0
            if l1!=None: va=l1.val
            if l2!=None: vb=l2.val
            v = v0 + va + vb
            v0=int(v/10)
            l4.next = ListNode(v%10)
            l4 = l4.next
            if l1!=None: l1=l1.next
            if l2!=None: l2=l2.next
        return l3

l1=ListNode(2)
l1.next=ListNode(4)
l1.next.next=ListNode(3)
l2=ListNode(5)
l2.next=ListNode(6)
l2.next.next=ListNode(4)
v=addTwoNumbers(l1,l2)
print('%i %i %i'%(v.val,v.next.val,v.next.next.val))

