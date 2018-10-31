#Made By Sean Meyer on October 30, 2018;
#Physics Vector Math;
import math
import Vector


def getAngle(Ax = "none",Ay = "none"):
            if Ax == "none": Ax = float(input('Ax = '))
            if Ay == "none": Ay = float(input('Ay = '))
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

def getMagnitude(Ax = "none",Ay = "none"):
        if Ax == "none": Ax = float(input('Ax = '))
        if Ay == "none": Ay = float(input('Ay = '))
        return math.sqrt((Ax*Ax)+(Ay*Ay))

def AnalyticToPolar(xComp = "none",yComp = "none"):
        if xComp == "none": xComp = float(input('xComp = '))
        if yComp == "none": yComp = float(input('yComp = '))
        mag = str(getMagnitude(xComp,yComp))
        ang = str(
            getAngle(xComp,yComp))
        return mag + " @ "+ang


def polarToAnalytic(mag = "none",ang = "none"):
    if mag == "none": mag = float(input('Magnitude = '))
    if ang == "none": ang = float(input('ang = '))
    
    cosa = math.cos(math.radians(ang))
    x = mag*cosa
    sina = math.sin(math.radians(ang))
    y = mag*sina
    return "i: "+str(x)+" | "+"j: "+str(y)



def makeVectorPolar(mag = "none",ang = "none"):
    if mag == "none": mag = float(input('Magnitude = '))
    if ang == "none": ang = float(input('Angle = '))
    v = Vector.vector(mag,ang)
    return v

def makeVectorAnalytic(i= "none",j = "none"):
    if i == "none": i = float(input('i = '))
    if j == "none": j = float(input('j = '))
    v = Vector.vector(4,4)
    v.defineFromAnalytic(i,j)
    return v









vectors = list()


run = True
while run:
    print("Select a method to run:")
    print("1 : getAngle\t2 : getMagnitude\t3 : AnalyticToPolar")
    print("4 : polarToAnalytic\t5 : createNewVector\t6 : viewVectorList")
    print("7 : sumVectorList\t8 : resetVectorList\t9 : exit")
    methods = [1,2,3,4,5,6,7,8,9]
    
     #----------------------------------------------------------------
    choice = int(input("Run Method:\t"))
    while not(choice in methods):
        choice = int(input("Run Method:\t"))

    print("\t")
    #----------------------------------------------------------------
    while choice == 1:
        print(getAngle())
        print("\t")
        if not (input("Repeat calculation?\t") == "yes"):
            choice = "ENDING"
    #----------------------------------------------------------------
    while choice == 2:
        print(getMagnitude())
        print("\t")
        if not (input("Repeat calculation?\t") == "yes"):
            choice = "ENDING"
    #----------------------------------------------------------------
    while choice == 3:
        print(AnalyticToPolar())
        print("\t")
        if not (input("Repeat calculation?\t") == "yes"):
            choice = "ENDING"
    #----------------------------------------------------------------
    while choice == 4:
        print(polarToAnalytic())
        print("\t")
        if not (input("Repeat calculation?\t") == "yes"):
            choice = "ENDING"
    #----------------------------------------------------------------
    while choice == 5:
        c = int(input("1 : polar or 2 : analytic?\t")) 
        if ( c == 1):
            vectors.append(makeVectorPolar())
        elif (c == 2):
            vectors.append(makeVectorAnalytic())
        print("\t")
        if not (input("add another?\t") == "yes"):
            choice = "ENDING"
    #----------------------------------------------------------------
    while choice == 6:
        print("Stored Vectors:")
        for i in range(len(vectors)):
            print(vectors[i].toPolarString())
        choice = "ENDING"
    #----------------------------------------------------------------
    while choice == 7:
        print("Sumed Vectors:")
        i = 0
        v = Vector.vector(0,0)
        while i < (len(vectors)):
            v.add(vectors[i])
            i = i+1
        print("Analytic: "+vectors[0].toAnalyticString())
        print("Polar: "+vectors[0].toPolarString())
        choice = "ENDING"


##        while choice == 7:
##        print("Sumed Vectors:")
##        i = 1
##        while i < (len(vectors)):
##            vectors[0].add(vectors[i])
##            i = i+1
##        print("Analytic: "+vectors[0].toAnalyticString())
##        print("Polar: "+vectors[0].toPolarString())
##        choice = "ENDING"

    #----------------------------------------------------------------
    while choice == 8:
        print("Reset Vectors")
        vectors = list()
        choice = "ENDING"
    #----------------------------------------------------------------
    print("\t")
    if choice == 9:
        run = False

