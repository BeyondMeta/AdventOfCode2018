# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 13:08:53 2018

@author: Sophie
"""
import re

newList = []
file = open("C:/Users/Sophie/Documents/PythonScripts/input4.txt", "r")
for line in file:
    newList.append(line)
 
newList.sort()
#print(newList)

testList = ["[1518-11-01 00:00] Guard #10 begins shift",
"[1518-11-01 00:05] falls asleep",
"[1518-11-01 00:25] wakes up",
"[1518-11-01 00:30] falls asleep",
"[1518-11-01 00:55] wakes up",
"[1518-11-01 23:58] Guard #99 begins shift",
"[1518-11-02 00:40] falls asleep",
"[1518-11-02 00:50] wakes up",
"[1518-11-03 00:05] Guard #10 begins shift",
"[1518-11-03 00:24] falls asleep",
"[1518-11-03 00:29] wakes up",
"[1518-11-04 00:02] Guard #99 begins shift",
"[1518-11-04 00:36] falls asleep",
"[1518-11-04 00:46] wakes up",
"[1518-11-05 00:03] Guard #99 begins shift",
"[1518-11-05 00:45] falls asleep",
"[1518-11-05 00:55] wakes up"]

def sleepingGuard(lst):
    myDict = {}
    for i in lst:
        if "Guard" in i: 
            guardNum= int(re.search('#(.*?) ', i).group(1))
        elif "falls" in i:    
            fallAsleep =  int(re.search(':(.*?)]', i).group(1))
        else:
            wakesUp = int(re.search(':(.*?)]', i).group(1))
            if guardNum in myDict:
                myDict[guardNum][fallAsleep:wakesUp] = [v+1 for v in myDict[guardNum][fallAsleep:wakesUp]]            
            else:
                myDict[guardNum] = [0]*60
                myDict[guardNum][fallAsleep:wakesUp] = [v+1 for v in myDict[guardNum][fallAsleep:wakesUp]] 
    Max = 0
    sleepiestGuard = 0
    for i in myDict:
        guardSleep = max(myDict[i])
        if guardSleep > Max:
            Max = guardSleep
            sleepiestGuard = i
    return [sleepiestGuard, myDict[sleepiestGuard].index(max(myDict[sleepiestGuard]))]

print( sleepingGuard(newList))
print(sleepingGuard(testList))