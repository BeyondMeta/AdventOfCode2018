# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 21:42:34 2019

@author: Sophie
"""
myList = []
file = open("C:/Users/Sophie/Documents/PythonScripts/input8.txt", "r")
for line in file:
    myList.append(line)
    
myList = myList.split(" ")
myList = list(map(int, myList))


class metaTree(object):
     def __init__(self, name='root', children=None, numChild, numMetaData, metaData):
         self.name = name
         self.numChild
         self.metaData = []
         self.numMetaData =0
         self.children = []
         if children is not None:
             for child in children:
                 self.add_child(child)
     
     def __repr__(self):
         return self.name
     def add_child(self, node):
         assert isinstance(node, metaTree)
         self.children.append(node)
    
def constructTree(lst):
    myList = lst
    while lst:
        metaTree()

    
 
