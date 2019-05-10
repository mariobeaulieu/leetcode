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
        #if id1<id2:
            self.listNodes[id1].connect(self.listNodes[id2])
        #else:
            self.listNodes[id2].connect(self.listNodes[id1])
    def scanAllNodes(self, nodeId:int, prevId:int):
        ptrNode=self.listNodes[nodeId]
        # Now update distances with all previously visited nodes:
        #print('Current=%i, visited='%nodeId,self.visited)
        for v in self.visited:
            d=self.distances[v][prevId]+1
            self.distances[nodeId][v]=self.distances[v][nodeId]=d
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
    def findMinHeightTrees(self) -> List[int]:
        myMin=max(self.distances[0])
        myMins=[0]
        for i in range(1,self.n):
            m=max(self.distances[i])
            if m<myMin:
                myMins=[i]
                myMin=m
            elif m==myMin:
                myMins.append(i)
        return myMins
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n<1: return []
        if n==1:return [0]
        if n==2:return [0,1]
        t = Tree(n)
        #edges.sort()
        #print(edges)
        for pair in edges:
            t.linkNodes(pair[0],pair[1])
        t.scanAllNodes(0,-1)
        #t.printDistances()
        return t.findMinHeightTrees()

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
    #print (myList)
    print ('Head nodes for minimum height trees:',s.findMinHeightTrees(n,myList))
