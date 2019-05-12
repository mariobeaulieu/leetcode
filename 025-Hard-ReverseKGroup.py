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
    def reverseKGroup(self, head: ListNode, k:int) -> ListNode:
        newHead=head
        if head==None or head.next==None: return head
        prevNode=None
        done=False
        while head!=None:
            myList=[]
            for i in range(k):
                if head==None:
                    done=True
                    break
                myList.append(head)
                head=head.next
            # We save the location pointed by the last node of this segment
            if done: break
            tmpNode=myList[-1].next
            # The node that pointed to the beginning of this segment must now point to the last of it
            if prevNode==None:
                newHead=myList[-1]
            else:
                prevNode.next=myList[-1]
            for j in range(i, 0, -1):
                myList[j].next=myList[j-1]
            myList[0].next=tmpNode
            prevNode=myList[0]
        return newHead

if __name__=='__main__':
    try:
        n=int(sys.argv[1])
        g=int(sys.argv[2])
    except:
        print('Program to flip nodes in groups')
        print(' 1->2->3->4->5->6->7->8 in groups of 3 becomes 3->2->1->6->5->4->7->8')
        print('Usage: %s <Number of nodes> <group size>'%sys.argv[0])
        sys.exit(-1)
    node=node0=ListNode(0)
    for i in range(1,n+1):
        node.next = ListNode(i)
        node = node.next
    print('Initial list: ',end='')
    node=node0.next
    node.printIt()
    s=Solution()
    print('Flipped list: ',end='')
    node2=s.reverseKGroup(node,g)
    node2.printIt()
