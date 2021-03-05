import matplotlib.pyplot as plt
import numpy as np
import time
import random
from math import exp, expm1,sin,atan,sqrt,cos
import matplotlib.tri as tri
from matplotlib.patches import Polygon
from matplotlib import animation



class nokta:
      x = 0.0
      y = 0.0
      foo = 0.0
      count = 0
      success = 'B'


def op(x,y):

    return sqrt(x*x + y*y)


def bp(x,y):

    return sqrt(x*x + (y - 1)*(y - 1))


def cp(x,y):

   return sqrt((x - 2)*(x - 2) + (y - 1)*(y - 1))



def v(x,y):

    #return ((op(x,y) - 0.5)*(op(x,y) - 0.5)) + 2*((bp(x,y) - 0.5)*(bp(x,y) - 0.5)) + 3*((cp(x,y) - 0.5)*(cp(x,y) - 0.5))
    return 1.0 + ((((x*x)/4000) + ((y*y)+4000)) - (cos(x/sqrt(1))*cos(y/sqrt(2))))

def ort(x1,x2) :

    return 0.5*(x1 + x2)

def reflect(x,xort) :
    
    return x + 2*(xort - x)


def control(n1,n2,n3) :

    if(n1.success == 'B'):

        if(n2.success == 'B' or n3.success == 'B'):

            if(n2.success == 'B') :

                if(n3.success == 'B') :

                    if(n1.foo>n2.foo and n1.foo>n3.foo):

                        return True
                    else :
                        return False
                else :

                    if(n1.foo > n2.foo):

                        return True
                    else :
                        return False

            else :

                if(n1.foo > n3.foo) :

                    return True
                
                else :

                    return False


        else :

            return True
    
    else :

        return False




def simlex(n1,n2,n3,h,hata) :
    
    sayac = 0

    plt.axes(xlim=(-1,10), ylim=(-1, 10))
    plt.grid(b=None, which='major', axis='both')


    points = [[n1.x, n1.y], [n2.x, n2.y], [n3.x, n3.y]]
    polygon = plt.Polygon(points,fill=None)
    plt.gca().add_patch(polygon)
    plt.pause(1e-17)
    time.sleep(0.5)


    count = 0
    while(h > hata):
        
        count = count + 1
        

        print("******simplex*******")
        print("n1  x:  " + str(n1.x)  +  "  y  :"+str(n1.y) + "    f  :  " +  str(n1.foo) + "  success  :   "  + n1.success  + "   count :" + str(n1.count))
        print(" ")
        print("n2  x:  " + str(n2.x)  +  "  y  :"+str(n2.y) + "    f  :  " +  str(n2.foo) + "  success  :   "  + n2.success  + "   count :" + str(n2.count))
        print(" ")
        print("n3  x:  " + str(n3.x)  +  "  y  :"+str(n3.y) + "    f  :  " +  str(n3.foo) + "  success  :   "  + n3.success  + "   count :" + str(n3.count))
        print(" ")
        print(" ")
        print(" ")
        print(" ")

        if(control(n1,n2,n3)) :

            #print("geldim sıra1 :" + str(sayac))
            sayac = sayac + 1
            
                #print("geldim sır2 :" + str(sayac))
              
            #else :
                #print("geldim sıra3 :" + str(sayac))
            sayac = sayac + 1
            xort = ort(n2.x,n3.x)
            n1.x = reflect(n1.x,xort)

            yort = ort(n2.y,n3.y)
            n1.y = reflect(n1.y,yort)
            n1.foo = v(n1.x,n1.y)
            n1.count = 1
            n2.count = n2.count + 1
            n3.count = n3.count + 1

            if(n1.foo > n2.foo and n1.foo > n3.foo) :
                n1.success = 'F'
            else :
                n1.success = 'B'
            n2.success = 'B'
            n3.success = 'B'

            points = [[n1.x, n1.y], [n2.x, n2.y], [n3.x, n3.y]]
            polygon = plt.Polygon(points,fill=None)
            plt.gca().add_patch(polygon)
            plt.pause(1e-17)
            time.sleep(0.5)
            if(n2.count == 4):
                h = h/2

                n1.x = (n2.x + n1.x)/2
                n1.y = (n2.y + n1.y)/2
                n1.foo  = v(n1.x,n1.y)
                n1.count = 1
                n1.success = 'B'

                n3.x = (n3.x + n2.x)/2
                n3.y = (n3.y + n2.y)/2
                n3.foo  = v(n3.x,n3.y)
                n3.count = 1
                n3.success = 'B'
                n2.success = 'B'
                n2.count = 1

                points = [[n1.x, n1.y], [n2.x, n2.y], [n3.x, n3.y]]
                polygon = plt.Polygon(points,fill=None)
                plt.gca().add_patch(polygon)
                plt.pause(1e-17)
                time.sleep(0.5)

            elif(n3.count == 4):
    
                h = h/2

                n1.x = (n1.x + n3.x)/2
                n1.y = (n1.y + n3.y)/2
                n1.foo  = v(n1.x,n1.y)
                n1.count = 1
                n1.success = 'B'

                n2.x = (n2.x + n3.x)/2
                n2.y = (n2.y + n3.y)/2
                n2.foo = v(n2.x,n2.y)
                n2.count = 1
                n2.success = 'B'
                n3.success = 'B'
                n3.count = 1
               
                points = [[n1.x, n1.y], [n2.x, n2.y], [n3.x, n3.y]]
                polygon = plt.Polygon(points,fill=None)
                plt.gca().add_patch(polygon)
                plt.pause(1e-17)
                time.sleep(0.5)

        elif (control(n2,n1,n3)) :
            #print("geldim sıra4 :" + str(sayac))
            sayac = sayac + 1
            
            #else :
                #print("geldim sıra6 :" + str(sayac))
            sayac = sayac + 1
            xort = ort(n1.x,n3.x)
            n2.x = reflect(n2.x,xort)

            yort = ort(n1.y,n3.y)
            n2.y = reflect(n2.y,yort)
            n2.foo = v(n2.x,n2.y)
            n2.count = 1
            n1.count = n1.count + 1
            n3.count = n3.count + 1

            if(n2.foo > n1.foo and n2.foo > n3.foo) :
                n2.success = 'F'
            else :
                n2.success = 'B'
            
            n1.success = 'B'
            n3.success = 'B'

            points = [[n1.x, n1.y], [n2.x, n2.y], [n3.x, n3.y]]
            polygon = plt.Polygon(points,fill=None)
            plt.gca().add_patch(polygon)
            plt.pause(1e-17)
            time.sleep(0.5)

            if(n1.count == 4):
                h = h/2

                n2.x = (n1.x + n2.x)/2
                n2.y = (n1.y + n2.y)/2
                n2.foo =  v(n2.x,n2.y)
                n2.count = 1
                n2.success = 'B'

                n3.x = (n1.x + n3.x)/2
                n3.y = (n1.y + n3.y)/2
                n3.foo  = v(n3.x,n3.y)
                n3.count = 1
                n3.success = 'B'
                n1.success = 'B'

                n1.count = 1

                points = [[n1.x, n1.y], [n2.x, n2.y], [n3.x, n3.y]]
                polygon = plt.Polygon(points,fill=None)
                plt.gca().add_patch(polygon)
                plt.pause(1e-17)
                time.sleep(0.5)

            elif(n3.count == 4):
        
                h = h/2

                n1.x = (n1.x + n3.x)/2
                n1.y = (n1.y + n3.y)/2
                n1.foo  = v(n2.x,n2.y)
                n1.count = 1
                n1.success = 'B'

                n2.x = (n2.x + n3.x)/2
                n2.y = (n2.y + n3.y)/2
                n2.foo = v(n2.x,n2.y)
                n2.count = 1
                n2.success = 'B'
                n3.success = 'B'
                n3.count = 1

                points = [[n1.x, n1.y], [n2.x, n2.y], [n3.x, n3.y]]
                polygon = plt.Polygon(points,fill=None)
                plt.gca().add_patch(polygon)
                plt.pause(1e-17)
                time.sleep(0.5)

        else :
            
            
                #print("geldim sıra8 :" + str(sayac))
            #else :
                #print("geldim sıra10 :" + str(sayac))
            xort = ort(n1.x,n2.x)
            n3.x = reflect(n3.x,xort)

            yort = ort(n1.y,n2.y)
            n3.y = reflect(n3.y,yort)
            n3.foo = v(n3.x,n3.y)
            n3.count = 1
            n1.count = n1.count + 1
            n2.count = n2.count + 1

            if(n3.foo > n1.foo and n3.foo > n2.foo) :
                n3.success = 'F'
            else :
                n3.success = 'B'
            n1.success = 'B'
            n2.success = 'B'

            points = [[n1.x, n1.y], [n2.x, n2.y], [n3.x, n3.y]]
            polygon = plt.Polygon(points,fill=None)
            plt.gca().add_patch(polygon)
            plt.pause(1e-17)
            time.sleep(0.5)

            if(n1.count == 4):
                h = h/2

                n2.x = (n1.x + n2.x)/2
                n2.y = (n1.y + n2.y)/2
                n2.foo =  v(n2.x,n2.y)
                n2.count = 1
                n2.success = 'B'

                n3.x = (n1.x + n3.x)/2
                n3.y = (n1.y + n3.y)/2
                n3.foo  = v(n3.x,n3.y)
                n3.count = 1
                n3.success = 'B'
                n1.success = 'B'

                n1.count = 1

                points = [[n1.x, n1.y], [n2.x, n2.y], [n3.x, n3.y]]
                polygon = plt.Polygon(points,fill=None)
                plt.gca().add_patch(polygon)
                plt.pause(1e-17)
                time.sleep(0.5)

            elif(n2.count == 4):
                h = h/2

                n1.x = (n2.x + n1.x)/2
                n1.y = (n2.y + n1.y)/2
                n1.foo  = v(n2.x,n2.y)
                n1.count = 1
                n1.success = 'B'

                n3.x = (n3.x + n2.x)/2
                n3.y = (n3.y + n2.y)/2
                n3.foo  = v(n3.x,n3.y)
                n3.count = 1
                n3.success = 'B'
                n2.success = 'B'
                n2.count = 1

                points = [[n1.x, n1.y], [n2.x, n2.y], [n3.x, n3.y]]
                polygon = plt.Polygon(points,fill=None)
                plt.gca().add_patch(polygon)
                plt.pause(1e-17)
                time.sleep(0.5)

    print("iterasyon sayısı  :" ,str(count))
    print("son  uzunluk sayısı  :" ,str(h))

n1 = nokta()
n2 = nokta()
n3 = nokta()

hata = float(input ("Hata miktarı giriniz  :"))
h = float(input ("Uzunluk giriniz  :"))


n1.x = float(input ("x koordinatı giriniz  :"))
n1.y = float(input ("y koordinatı giriniz  :"))
n1.count = 1
n1.success = 'B'
n1.foo = v(n1.x,n1.y)

n2.x = n1.x
n2.y = n1.y + h
n2.count = 1
n2.success = 'B'
n2.foo = v(n2.x,n2.y)

n3.y = (n1.y + n2.y)/2
n3.x = sqrt(h*h - (n3.y - n1.y)*(n3.y - n1.y))
n3.count = 1
n3.success = 'B'
n3.foo = v(n3.x,n3.y)



simlex(n1,n2,n3,h,hata)


plt.show()



