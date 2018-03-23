# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Ractangle :
    width =0
    hight =0

    def surround(self):
        ans = 2*(self.width+self.hight)
        return ans
    def area(self):
        Area = self.hight*self.width
        return Area 
    pass

a=Ractangle()
b=Ractangle()

a.width=30
a.hight=10

b.width=40
b.hight=27
max_surround = max(a.surround(),b.surround())
if max_surround == a.surround():
    print("a")
else:
    print('b')
    
   
max_area = max(a.area(),b.area())
if max_area == a.area():
    print("a")
else:
    print('b')


