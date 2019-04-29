#!/usr/bin/env python

import sys
from typing import List

class Solution:
    def trap(self,height: List[int]) -> int:
        volume    = 0
        # List of left walls (pos,height) that are not filled to their height
        leftWalls = [(0,height[0])]
        # This is the level from the last column
        currLevel  = height[0]
        for p in range(1,len(height)):
            h = height[p]
            ph= leftWalls[-1][1]
            print('Pos %i: height is %i, current level at %i and previous height is %i, walls='%(p,h,currLevel,ph),leftWalls)
            if  h<=currLevel:
                # We add this wall to the list of left walls, but
                # if it's the same as previous, we replace previous
                if h==currLevel:
                    leftWalls.pop()
                leftWalls.append((p,h))
                currLevel = h
                print('Lower wall at level %i and pos %i. List of walls is now'%(h,p),leftWalls)
            else:
                (x,y)=leftWalls.pop()
                print('Popped (%i,%i), leftWalls='%(x,y),leftWalls)
                while h>currLevel:
                    if len(leftWalls)==0:
                        leftWalls.append((p,h))
                        currLevel = h
                        print('Only 1 wall now: ',leftWalls)
                    else:
                        #We need to fill to the nearest left wall
                        (x,y)=leftWalls[-1]
                        volume += (min(y,h)-currLevel)*(p-x-1)
                        level=min(y,h)
                        print('Pos %i: just added %i to the volume. Current level now at %i, new volume at %i, leftWalls='%(p,(level-currLevel)*(p-x-1),level,volume),leftWalls) 
                        currLevel = level
                        if h>=y:
                            # The current wall should replace the last left wall
                            leftWalls.pop()
                # Add the current wall to the list
                leftWalls.append((p,h))
        return volume

if len(sys.argv)<4:
    print('Usage: %s <list of wall heights to collect rain water>'%sys.argv[0])
else:
    S=Solution()
    heights = list(map(int, sys.argv[1:]))
    print('Volume is %i'%S.trap(heights))
