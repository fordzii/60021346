# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 13:24:28 2018

@author: Student
"""

def CalculateSomething(n):
    if n == 1 :
        return 1
    else : 
        return 1/n + CalculateSomething(n-1)

