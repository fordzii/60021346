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

class Student :
    First_Name =""
    Last_Name = ""
    ID = ""
    Score = int()
    
    def calGrade (self):
        if self.Score < 50 :
            return "F"
        elif self.Score >= 50 :
            return "P"
        elif self.Score >= 70 :
            return "X"
    def compareStudent(self,anotherStudent : "Student") -> "Student" : 
        max_score = max(self.Score,anotherStudent.Score)
        if max_score == anotherStudent.Score :
            return anotherStudent
        elif self == max_score == anotherStudent:
            return self,anotherStudent
        else :
            return self
 
a = Student()
a.First_Name ="fish"
a.Last_Name = "wdwddwd"
a.ID = "4648884"
a.Score = 45
print("This is a grade = ",a.calGrade())

b = Student()
b.First_Name ="ford"
b.Last_Name = "fofrd"
b.ID = "60021346"
b.Score = 62
print("This is a grade = ",b.calGrade())

scorethenAB = a.compareStudent(b)
print("Is more score :",scorethenAB) 