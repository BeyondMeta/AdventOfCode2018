# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 20:06:32 2019

@author: Sophie
"""
from collections import deque

def stupidMarbleGame(players, turns):
    playersScore = [0] * players
    #scores = defaultdict(int)
    marbles = deque([0])
    #currentMarble = 0
    for i in range(1, turns * 100 +1):
        if i % 23 == 0:
            marbles.rotate(7)
            #index =(currentMarble - 7) % len(marbles) 
            playersScore[i % players] += i + marbles.pop()
            #scores[i % players]
            marbles.rotate(-1)
            #currentMarble = (currentMarble -6) % len(marbles)
        else:
            marbles.rotate(-1)
            marbles.append(i)
    
    return max(playersScore)

print("Test inputs")
print(stupidMarbleGame(10, 1618))
print(stupidMarbleGame(13, 7999))
print(stupidMarbleGame(17, 1104))
print(stupidMarbleGame(21, 6111))

print(stupidMarbleGame(462, 71938))