# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 14:57:55 2018

@author: Sophie
"""
from collections import Counter

myList = []
file = open("C:/Users/Sophie/Documents/PythonScripts/input6.txt", "r")
for line in file:
    line= line.split(",")
    myList.append([int(line[0]), int(line[1])]) 
                    
    
def boundingBox(lst):
    minXY = [lst[0][0], lst[0][1]]
    maxXY = [lst[0][0], lst[0][1] ]
    for i in lst:
        if i[0] < minXY[0]:
           # print("a")
            minXY[0] = i[0]
        if i[1] < minXY[1]:
            #print("b")
            minXY[1] = i[1]
        if i[0] > maxXY[0]:
            #print("c")
            maxXY[0] = i[0]
        if i[1] > maxXY[1]:
            #print("d")
            maxXY[1] = i[1]
    
    print([minXY, maxXY])
    return [minXY, maxXY]
    

Test = [[1,1], [1,6], [8,3], [3, 4], [5, 5],[8,9]]
    
def printList(lst):
    for i in lst:
        print(i)        
        
#print(boundingBox(myList))    

def taxicabGeo(a, b):
    c= abs(a[0] - b[0]) + abs(a[1] - b[1])
    return c

def CalculateArea(lst):
    myBB = boundingBox(lst)
    pointList = []
    OutofBound = []
    for i in range(myBB[0][0],myBB[1][0] +1):
        for j in range(myBB[0][1], myBB[1][1] + 1):
            newList =[]
            for k in lst:
                newList.append(taxicabGeo([i, j], k))
            myMin = min(newList)
            if newList.count(myMin) ==1:            
                 if i == myBB[0][0] or i ==myBB[1][0] or j==myBB[0][1] or j ==myBB[1][1]:
                     OutofBound.append(newList.index(myMin))
                 else:
                    pointList.append(newList.index(myMin))
            else:
                pointList.append(-1)
    data = Counter(pointList)
    
    print("These points are: ", set(OutofBound))
    return data.most_common()


def CalculateArea2(lst):
    myBB = boundingBox(lst)
    pointList = []
    for i in range(myBB[0][0],myBB[1][0] +1):
        for j in range(myBB[0][1], myBB[1][1] + 1):
            total = 0
            for k in lst:
                total = total + taxicabGeo([i, j], k)
            pointList.append(total)
    return sum(num < 10000 for num in pointList )
    
    

        
#print(CalculateArea(Test))               
print(CalculateArea2(myList))