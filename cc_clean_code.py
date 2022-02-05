# -*- coding: utf-8 -*-
"""
20b6001, Nadeeya
clean-coding
clean code examples
"""
import math
#Intention-revealing names:
    
def fallingDistance(time):
    gravity = 9.8
    distance = (0.5)*gravity*math.pow(time, 2)
    print(distance)

#avoid disinformation
def commonfactor(num1, num2):
    minNum = min(num1,num2)
    greatestCommonDiv = 1
    divisor = 1
    while (divisor <= minNum):
        if ((num1%divisor==0) and (num2%divisor==0)):
            greatestCommonDiv = divisor
            
        divisor+=1
        
    return greatestCommonDiv

#make meaningful distictions
def testscore (studentAge , studentScore):
    if (studentAge > 10):
        if studentScore >= 50:
            print("You passed!")
            
        else:
            print("You failed")
            
    else:
        print("You're too young to take the test.")
        
#use pronouncable name:
    
def sphereSurfaceArea(vol):
    rad = math.pow((vol*3/(4*math.pi)), 1/3)
    rad2DecimalPlaces = round(rad,2)
    
    surfaceArea = 4*math.pi*math.pow(rad,2)
    sArea2DecimalPlaces = round(surfaceArea, 2)
    print('Surface area of the sphere with the given volume is ', sArea2DecimalPlaces)
    
#use searchable names
def time(sec):
    hour = sec/3600
    minute = sec%3600/60
    sec2 =sec%3600%60
    
    print(sec , " seconds is ", hour ," hr, ", minute, " min and ", sec2, " seconds.")
    
#class method names. (dont be cute)
#pick one word per concept 
class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width 
        
    def getLength(self):
        return self.length
    
    def getWidth(self): 
        return self.width
    
    def changeLength(self, length): 
        self.length = length
        return self.length
    
    def changeWidth(self, width):
        self.width = width
        return self.width 
    
#add meaningful context
def membership(points):
    if points==0:
        member , discount = notmember()
        
    elif points<=100:
        member , discount = classicMember() 
        
    elif points<=150:
        member , discount = executiveMember() 

    else: 
        member , discount = prestigiousMember() 
        
    print("you are ", member, " member. You will have ", discount, " discount.")
        
def notmember():
    member = "not"
    discount = "no"
    return member , discount 

def classicMember():
    member = "a classic"
    discount = "10%"
    return member, discount

def executiveMember():
      member = "an executive"
      discount = "15%"
      return member, discount
  
def prestigiousMember():
        member = "a prestigious"
        discount = "20%"
        return member, discount
    





        
        
    
