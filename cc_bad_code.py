
"""
20b6001, Nadeeya
clean-coding
bad coding examples
"""
import math

#Intention-revealing names:
    
def fd(t):
    g = 9.8
    d = (0.5)*g*math.pow(t, 2)
    print(d)

#avoid disinformation
def commonfactor(l, i):
    s = min(l,i)
    gcd = 1
    O = 1
    while (O <= s):
        if ((l%O==0) and (i%O==0)):
            gcd = O
            
        O+=1
        
    return gcd

#make meaningful distictions
def testscore (studentA , studentS):
    if (studentA > 10):
        if studentS >= 50:
            print("You passed!")
            
        else:
            print("You failed")
            
    else:
        print("You're too young to take the test.")
        
#use pronouncable name:
    
def sphSfrAr(vol):
    rad = math.pow((vol*3/(4*math.pi)), 1/3)
    r2dcmplc = round(rad,2)
    
    sfrAr = 4*math.pi*math.pow(rad,2)
    s2dcmplc = round(sfrAr, 2)
    print('Surface area of the sphere with the given volume is ', s2dcmplc)
    
#use searchable names
def t(s):
    h = s/3600
    m = s%3600/60
    s2 =s%3600%60
    
    print(s , " seconds is ", h ," hr, ", m, " min and ", s2, " seconds.")
    

#class method names. (dont be cute)
#pick one word per concept 
class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width 
        
    def getLength(self):
        return self.length
    
    def retrieveWidth(self): #using a different word for the get functions
        return self.width
    
    def lengthMakeOver(self, length): #not naming the function profesionally or formally
        self.length = length
        return self.length
    
    def changeWidth(self, width):
        self.width = width
        return self.width
    
#add meaningful context
def membership(points):
    if points==0:
        member = "not"
        discount = "no"
        
    elif points<=100:
        member = "a classic"
        discount = "10%"
        
    elif points<=150:
        member = "an executive"
        discount = "15%"
        
    else: 
        #greater than 150 points
        member = "a prestigious"
        discount = "20%"
        
    print("you are ", member, " member. You will have ", discount, " discount.")
    
    


    
    

    
    





