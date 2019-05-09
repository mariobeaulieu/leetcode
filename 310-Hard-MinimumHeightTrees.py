#!/usr/bin/env python

import sys
from typing import List

class Node:
    def __init__(self, nodeId:int):
        self.nodeId = nodeId
        self.ptrs=[]
    def connect(self, ptr):
        self.ptrs.append(ptr)
class Tree:
    def __init__(self,n:int):
        self.listNodes=[]
        self.distances=[]
        self.visited  =[]
        self.n=n
        for i in range(n):
            node=Node(i)
            self.listNodes.append(node)
        self.distances=[[0 for i in range(n)] for j in range(n)]
    def linkNodes(self, id1:int, id2:int):
        self.listNodes[id1].connect(self.listNodes[id2])
        self.listNodes[id2].connect(self.listNodes[id1])
    def updateDistance(self,id1,id2,v):
        if self.distances[id1][id2]!=0:
            print ('Modifying distance from %i to %i was %i to %i'%(id1,id2,self.distances[id1][id2],v))
        self.distances[id1][id2]=self.distances[id2][id1]=v
    def scanAllNodes(self, nodeId:int, prevId:int):
        ptrNode=self.listNodes[nodeId]
        if prevId>=0:
            # Update the distance table with distance with the node just before
            self.updateDistance(nodeId,prevId,1)
        # Now update distances with all previously visited nodes:
        for v in self.visited:
            self.updateDistance(nodeId,v,self.distances[prevId][v]+1)
        self.visited.append(nodeId)
        # Now call recursively all other nodes connected to this one
        for newNode in ptrNode.ptrs:
            if newNode.nodeId != prevId:
                self.scanAllNodes(newNode.nodeId, nodeId)
    def printDistances(self):
        for i in range(self.n):
            for j in range(self.n):
                print('%3i '%self.distances[i][j],end='')
            print()
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n<1: return []
        if n==1:return [0]
        if n==2:return [0,1]
        t = Tree(n)
        for pair in edges:
            t.linkNodes(pair[0],pair[1])
        t.scanAllNodes(0,-1)
        t.printDistances()

if len(sys.argv)<2:
    print('Usage: %s <nbNodes> <list of edges>'%sys.argv[0])
    print('  Ex:  %s 5 0 1 0 2 2 3 2 4'%sys.argv[0])
    print('  That is 5 nodes labelled 0 to 4 and edges 0-1,0-2,2-3 and 2-4')
else:
    s=Solution()
    n=int(sys.argv[1])
    i=0
    myList=[]
    for c in sys.argv[2:]:
        if i==0:
            v1=int(c)
            i=1
        else:
            v2=int(c)
            myList.append([v1,v2])
            i=0
    print (myList)
    s.findMinHeightTrees(n,myList)
