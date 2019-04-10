# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 18:50:47 2018

@author: Sophie
"""
import re
from itertools import count
from string import ascii_lowercase


myList = []
myDict = {}
file = open("C:/Users/Sophie/Documents/PythonScripts/input7.txt", "r")
for line in file:

    key = (re.search('Step (.+?) must be', line).group(1))
    value = (re.search('step (.+?) can', line).group(1))
    if key in myDict:
        myDict[key].append(value)
        myDict[key].sort()
    else:
        myDict[key] = [value]
        
def letter_indexes(text):
    text = text.lower()

    letter_mapping = dict(zip(ascii_lowercase, count(1)))
    indexes = [
      letter_mapping[letter] for letter in text 
      if letter in letter_mapping
    ]

    return ' '.join(str(index) for index in indexes)
     
    
#print(myDict)

altDict = {}
file = open("C:/Users/Sophie/Documents/PythonScripts/input7.txt", "r")
for line in file:

    value = (re.search('Step (.+?) must be', line).group(1))
    key = (re.search('step (.+?) can', line).group(1))
    if key in altDict:
        altDict[key].append(value)
        altDict[key].sort()
    else:
        altDict[key] = [value]
    
print(altDict)

def RemoveDependency(dic, val):
    thingsToPop =[]
    for j in dic:
        if val in dic[j]:
                #print("Removing dependacy", newValue, "from ", j,  dic)
            dic[j].remove(val)
                #print(dic[j])
            if not dic[j]:
                thingsToPop.append(j)
    for i in thingsToPop:
            #print("Removing element ", i, dic)
        dic.pop(i)


def AssemblyInstructions(dic):
    alphabetString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    outputString = ""
    while alphabetString:
        startingPoint = []
        thingsToPop =[]
        for i in alphabetString:
            if not (i in dic):
                startingPoint.append(i)
                #print(i)
        startingPoint.sort()
        newValue = startingPoint[0]
        #print("newValue", newValue)
        outputString = outputString + newValue
        alphabetString =alphabetString.replace(newValue, "")
        for j in dic:
            if newValue in dic[j]:
                #print("Removing dependacy", newValue, "from ", j,  dic)
                dic[j].remove(newValue)
                #print(dic[j])
                if not dic[j]:
                    thingsToPop.append(j)
        for i in thingsToPop:
            #print("Removing element ", i, dic)
            dic.pop(i)
           
    
    return outputString

def AssemblyTime(dic):
    alphabetString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    completedTasks = ""
    timeSoFar = 0
    WorkersBusy =0 
    TaskInProgress = []
    while alphabetString:
        availableTasks = []    
        for i in alphabetString:
            if not (i in dic):
                availableTasks.append(i)
                #print(i)
        availableTasks.sort()
        while WorkersBusy < 5  and availableTasks:
            i = int(letter_indexes(availableTasks[0])) +60 + timeSoFar
            TaskInProgress.append([ availableTasks[0], i])
            availableTasks.pop(0)
            WorkersBusy =+ 1
        else : 
            newestCompletedTask = TaskInProgress[0][0]
            timeSoFar = TaskInProgress[0][1]
            TaskInProgress.pop(0)
            WorkersBusy =- 1
            RemoveDependency(dic, newestCompletedTask)
            completedTasks = completedTasks + newestCompletedTask
            alphabetString =alphabetString.replace(newestCompletedTask, "")
            print(alphabetString)

    return timeSoFar
        
print(AssemblyTime(altDict))


            
#def AvailableTasks():
    #completedTasks = completedTasks + newestCompletedTask
    #alphabetString =alphabetString.replace(newValue, "")