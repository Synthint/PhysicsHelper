#Made By Sean Meyer on October 30, 2018;
#Vector;
import math
class vector:
        angle = 0.1
        magnitude = 0.1
        def __init__(self,magnitude,angle):
                self.angle = angle
                self.magnitude = magnitude
                
        def getAngle(self):
                return self.angle
        def getMagnitude(self):
                return self.magnitude
        def toPolarString(self):
                return str(self.getMagnitude())+" @ "+str(self.getAngle())
        def toAnalyticString(self):
                return "i: "+str(self.getAnalyticX())+" | "+"j: "+str(self.getAnalyticY())

        def getAnalyticX(self):
            m = self.magnitude
            cosa = math.cos(math.radians(self.angle))
            x = m*cosa
            return x
        def getAnalyticY(self):
            m = self.magnitude
            sina = math.sin(math.radians(self.angle))
            y = m*sina
            return y

        def defineFromAnalytic(self,xComp,yComp):
            self.angle = self.getAnalyticAngle(xComp,yComp)
            self.magnitude = self.getAnalyticMagnitude(xComp,yComp)

        def add(self,vec):
            
            i = self.getAnalyticX()+vec.getAnalyticX()
            j = self.getAnalyticY()+vec.getAnalyticY()
            self.defineFromAnalytic(i,j)




        #----------------------------------------
        #----------------------------------------
        #----------------------------------------
        #----------------------------------------
        #----------------------------------------




        def getAnalyticAngle(self,Ax,Ay):
            if Ax == 0:
                    if Ay>0:
                            return 90
                    if Ay<0:
                            return 270
                    if Ay == 0:
                            return "ERROR: BOTH COMPONENTS = 0"
            #----------------------------------------
            a = math.degrees(math.atan(Ay/Ax))
            if Ax>0 and Ay>0:
                    return a
            elif Ax<0 and Ay>0:
                    a+=180
            elif Ax<0 and Ay<0:
                    a+=180
            elif Ax>0 and Ay<0:
                    a+=180
            return a

        def getAnalyticMagnitude(self,Ax,Ay):
            return math.sqrt((Ax*Ax)+(Ay*Ay))





