# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 22:03:49 2019

@author: Sophie
"""
import numpy


def powerLevel(gridSerial, dim):
    arr = numpy.zeros((dim + 1, dim +1))
    Max = -45
    maxCord = [0, 0, 0]
    for xCor in range(1, dim + 1):
        for yCor in range(1, dim +1):
            rackId = xCor + 10
            PowerLevel = (rackId * yCor + gridSerial)* rackId
            PowerLevel = PowerLevel - (PowerLevel % 100)
            arr[xCor,yCor] = ((PowerLevel/ 100) % 10) - 5
    for k in range(1, 30):
        for i in range(1, dim - k +1):
            for j in range(1, dim -2):
                val = arr[i:i+k,j:j+k].sum()
                if val > Max:
                    Max = val
                    maxCord = [Max, i, j, k]
            
    return maxCord

print("Real Deal: ", powerLevel(9995, 300))
#print("Desired answer is 119 and 12dim actual answer is: ", powerLevel(42, 300))
