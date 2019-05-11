#!/usr/bin/env python

import sys
from typing import List

class Node:
    def __init__(self, nodeId:int):
        self.nodeId = nodeId
        self.nbEdges= 0
        self.ptrs   = []
    def connect(self, ptr):
        self.ptrs.append(ptr)
        self.nbEdges+=1
class Tree:
    def __init__(self,n:int):
        self.listNodes=[]
        self.distances=[]
        self.visited  =[]
        self.n=n
        self.pathToLeaf={}
        self.longestPath=0
        self.longestPair=[]
        for i in range(n):
            node=Node(i)
            self.listNodes.append(node)
        self.distances=[[0 for i in range(n)] for j in range(n)]
    def linkNodes(self, id1:int, id2:int):
        self.listNodes[id1].connect(self.listNodes[id2])
        self.listNodes[id2].connect(self.listNodes[id1])
    def scanAllNodes(self, nodeId:int, prevId:int, pathFromZero:List[int]):
        print('Scanning node %i, coming from %i'%(nodeId,prevId))
        ptrNode=self.listNodes[nodeId]
        leaf   =(ptrNode.nbEdges==1)
        if leaf: print('Node %i is a leaf'%nodeId)
        # Now update distances with all previously visited nodes:
        #print('Current=%i, visited='%nodeId,self.visited)
        for v in self.visited:
            d=self.distances[v][prevId]+1
            self.distances[nodeId][v]=self.distances[v][nodeId]=d
            # If both nodes are leafs and their distance>ever, keep their id
            if d>self.longestPath and leaf and self.listNodes[v].nbEdges==1:
                self.longestPath=d
                self.longestPair=[nodeId,v]
                print('Longest pair:',self.longestPair)
        self.visited.append(nodeId)
        # Now call recursively all other nodes connected to this one
        if leaf:
            self.pathToLeaf[nodeId]=pathFromZero
        for newNode in ptrNode.ptrs:
            newId=newNode.nodeId
            if newId != prevId:
                self.scanAllNodes(newNode.nodeId, nodeId,pathFromZero+[newId])
    def printDistances(self):
        for i in range(self.n):
            for j in range(self.n):
                print('%3i '%self.distances[i][j],end='')
            print()
    def findMinHeightTrees(self) -> List[int]:
        #Root(s) of minHeight Tree is at middle of longest distance
        p1=self.pathToLeaf[self.longestPair[0]]
        p2=self.pathToLeaf[self.longestPair[1]]
        #Find the last common element in the 2 lists
        i=1
        while i<len(p1) and i<len(p2) and p1[i]==p2[i]:
            i+=1
        print('p1 is',p1[i-1:],' and p2 is',p2[i-1:])
        #Reverse p1 and merge lists
        i-=1
        n=len(p1)-i
        for j in range(n//2):
            p1[i+j],p1[len(p1)-1-j]=p1[len(p1)-1-j],p1[i+j]
        p=p1[i:]+p2[i+1:]
        ll=len(p)
        print('Merged lists:',p)
        if ll%2==0:
            return p[ll//2-1:ll//2+1]
        else:
            return [p[ll//2]]
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
        t.scanAllNodes(0,-1,[0])
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
