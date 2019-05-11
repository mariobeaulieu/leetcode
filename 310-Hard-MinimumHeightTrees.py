#!/usr/bin/env python

import sys
from typing import List

class Node:
    def __init__(self, nodeId:int):
        self.nodeId = nodeId
        self.nbEdges= 0
        self.ptrs   = []
        self.pathToZero=[]
    def connect(self, ptr):
        self.ptrs.append(ptr)
        self.nbEdges+=1
class Tree:
    def __init__(self,n:int):
        self.debug=False
        self.listNodes=[]
        self.listLeafs=[]
        self.n=n
        for i in range(n):
            node=Node(i)
            self.listNodes.append(node)
        #self.distances=[[0 for i in range(n)] for j in range(n)]
    def linkNodes(self, id1:int, id2:int):
        self.listNodes[id1].connect(self.listNodes[id2])
        self.listNodes[id2].connect(self.listNodes[id1])
    def scanAllNodes(self, nodeId:int, prevId:int, pathFromZero:List[int]):
        if self.debug: print('Scanning node %i, coming from %i'%(nodeId,prevId))
        ptrNode=self.listNodes[nodeId]
        leaf   =(ptrNode.nbEdges==1)
        if leaf and self.debug: print('Node %i is a leaf'%nodeId)
        # Now call recursively all other nodes connected to this one
        if leaf:
            ptrNode.pathToZero=pathFromZero
            self.listLeafs.append([len(pathFromZero),nodeId])
        for newNode in ptrNode.ptrs:
            newId=newNode.nodeId
            if newId != prevId:
                self.scanAllNodes(newNode.nodeId, nodeId,pathFromZero+[newId])
    def findMinHeightTrees(self) -> List[int]:
        #listLeafs contains tuples for each leaf [dist-to-0, nodeId]
        self.listLeafs.sort(reverse=True)
        maxDist=0
        maxPair=[]
        done=False
        for i,leaf1 in enumerate(self.listLeafs[:-1]):
            d1=leaf1[0]
            if d1<maxDist//2: break
            l1=self.listNodes[leaf1[1]].pathToZero
            for leaf2 in self.listLeafs[i+1:]:
                d2=leaf2[0]
                if d1+d2<maxDist:
                    done=True
                    break
                l2=self.listNodes[leaf2[1]].pathToZero
                l3=list(set(l1+l2))
                d3=len(l3)
                dist=2*d3-d1-d2
                if self.debug: print('Found distance between nodes %i,%i = %i'%(leaf1[1],leaf2[1],dist))
                if dist>maxDist:
                    maxDist=dist
                    maxPair=[leaf1[1],leaf2[1]]
            if done: break
        if self.debug: print('Pair found: %i,%i with distance %i'%(maxPair[0],maxPair[1],maxDist))
        p1=self.listNodes[maxPair[0]].pathToZero
        p2=self.listNodes[maxPair[1]].pathToZero
        #Find the last common element in the 2 lists
        i=1
        while i<len(p1) and i<len(p2) and p1[i]==p2[i]:
            i+=1
        if self.debug: print('p1 is',p1[i-1:],' and p2 is',p2[i-1:])
        #Reverse p1 and merge lists
        i-=1
        n=len(p1)-i
        for j in range(n//2):
            p1[i+j],p1[len(p1)-1-j]=p1[len(p1)-1-j],p1[i+j]
        p=p1[i:]+p2[i+1:]
        ll=len(p)
        if self.debug: print('Merged lists:',p)
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
        for pair in edges:
            t.linkNodes(pair[0],pair[1])
        t.scanAllNodes(0,-1,[0])
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
    print ('Head nodes for minimum height trees:',s.findMinHeightTrees(n,myList))
