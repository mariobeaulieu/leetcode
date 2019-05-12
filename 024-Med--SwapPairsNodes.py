#!/usr/bin/env python

import sys

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next= None
    def printIt(self):
        if self.next==None:
            print(self.val)
        else:
            print(self.val,end='->')
            self.next.printIt()

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head==None or head.next==None: return head
        node1=head
        newHead=node2=head.next
        while node2!=None:
            tmpNode=node2.next
            node2.next=node1
            if tmpNode==None:
                node1.next=None
                break
            else:
                #If there's only 1 node left, node1 points to it
                if tmpNode.next==None:
                    node1.next=tmpNode
                    break
                #Otherwise, node1 points to the second node
                node2=node1.next=tmpNode.next
                node1=tmpNode
        return newHead

if __name__=='__main__':
    if len(sys.argv)<2:
        print('Program to flip pairs of nodes')
        print(' 1->2->3->4  becomes 2->1->4->3')
        print('Usage: %s <Number of nodes>'%sys.argv[0])
    else:
        n=int(sys.argv[1])
        node=node0=ListNode(0)
        for i in range(1,n+1):
            node.next = ListNode(i)
            node = node.next
        print('Initial list: ',end='')
        node=node0.next
        node.printIt()
        s=Solution()
        print('Flipped list: ',end='')
        node2=s.swapPairs(node)
        node2.printIt()
