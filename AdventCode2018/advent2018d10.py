# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 20:33:45 2019

@author: Sophie
"""
#import matplotlib.pyplot as plt
import re

myList = []
file = open("C:/Users/Sophie/Documents/PythonScripts/input10.txt", "r")
for line in file:
     x,y,vx,vy = map(int, re.findall('-?\d+', line))
     myList.append([x, y, vx, vy])
     
for t in range(20000):
    minx = min([x for x,y,_,_ in myList])
    maxx = max([x for x,y,_,_ in myList])
    miny = min([y for x,y,_,_ in myList])
    maxy = max([y for x,y,_,_ in myList])
      
field = [[' ']*(maxx-minx+1) for _ in range(maxy-miny+1)]      
for x, y, _, _ in myList:
    field[y-miny][x-minx] = '#'
    print('\n'.join(''.join(r) for r in field))
        
        
        
        
        
        
        
        
        

                    


#==============================================================================
# def secretMessage(lst):
#     for i in range(0, len(lst)):
#         xPos.append(int(re.search('position=<(.+?),', lst[i]).group(1)))
#         yPos.append(int(re.search(', (.+?)>', lst[i]).group(1)))
#         xVel.append(int(re.search('velocity=<(.+?),', lst[i]).group(1)))
#         yVel.append(int(re.search('velocity=<.., (.+?)>$', lst[i]).group(1)))
#     minBoundingBox = 100000000
#     for i in range(0, 20000):
#                 xVel = [x * i for x in xVel]
#                 yVel = [y * i for y in yVel]
#                 minx = min(x + y for x, y in zip(xPos, xVel))
#                 miny = min(x + y for x, y in zip(yPos, yVel))
#                 maxx = max(x + y for x, y in zip(xPos, xVel))
#                 maxy = max(x + y for x, y in zip(yPos, yVel))
#                 if minBoundingBox < maxx - minx + maxy - miny:
#                     minBoundingBox = maxx - minx + maxy - miny
#                     index = i
#                     print(minBoundingBox, index)
#     xVel = [x * index for x in xVel]
#     yVel = [y * index for y in yVel]
#     xPos = [x + y for x, y in zip(xPos, xVel)]
#     yPos = [x + y for x, y in zip(yPos, yVel)]
#     Map = [[' '] * 200 for j in range(0, 400)]
#     i = index
#     for i in range(0, len(xPos)):
#         Map[xPos[i]][yPos[i]] = '*'
# 
#     for m in map:
#         print(''.join(m))
#     #plt.plot(xPos, yPos, 'ro')
#==============================================================================
    
    
    
#secretMessage(myList)

