# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 10:11:58 2018

@author: Student
"""
#selection sort
L = [5,6,7,1,4,2,9,8,3]

'''
while(len(L) >0):
    minPos = 0
    minVal = L[minPos]
    for i in range(len(L)):
        if minVal > L[i]:
            minPos = i
            minVal = L[minPos]
    O.append(minVal) 
    L.pop(minPos)
    '''
#selection sort in memory
start = 0
while start < len(L):
    minPos = start
    minVal = L[minPos]
    for i in range(start,len(L)):
        if minVal > L[i]:
            minPos = i
            minVal = L[minPos]
    L[start],L[minPos] = L[minPos],L[start]
    start += 1
            