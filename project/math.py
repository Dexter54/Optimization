import matplotlib.pyplot as plt
import numpy as np

from math import exp, expm1,sin



def f(x):
    return pow(x,2) + 10*np.sin(x)

def der_f(x):
    return 2*x + 10*np.cos(x)



karar = 0
epoch = 0
step = 0
start = 0



def func(a,i):
    return (a+(2**i)*step)


def find_max(start,step,epochs)  :

    start_ilk = 999
    start_iki = 0
    for epoch in range(epochs):

        i = 0;
        x1 = f(start)
        i = i + 1
        x2 = f(start + i*step)
        i = i*2
        x3 = f(start + i*step)

        if(abs(start_ilk - start_iki)<0.001):
            break
        else :
            if(start_iki != 0)  :
                start_ilk = start_iki
    
        while True :
    
            if( x2 > x3 and  x2 >x1) :

                if(start_ilk == 999)  :
                    start_ilk = x2
                else  :
                    start_iki = x2

                i = i/2
                start = start + i*step
                step = step/10
                print("nokta  ve adım  :" , start , step )
                break
            else :
            
                i = i/2
                x1 = f(start + i*step) 
                i = i*2
                x2 = f(start + i*step)
                i = i*2
                x3 = f(start + i*step)

                print("x1  x2 x3 i:  ",x1,x2,x3,i)
    print("max nokta  :" ,  start)


def find_min(start,step,epochs)  :
        
    start_ilk = 999
    start_iki = 0

    for epoch in range(epochs):

        i = 0;
        x1 = f(start)
        i = i + 1
        x2 = f(start + i*step)
        i = i*2
        x3 = f(start + i*step)

        if(abs(start_ilk - start_iki)<0.01):
            break
        else :
            if(start_iki != 0)  :
                start_ilk = start_iki
    
        while True :
    
            if( x2 < x3 and  x2 < x1) :

                if(start_ilk == 999)  :
                    start_ilk = x2
                else  :
                    start_iki = x2

                i = i/2
                start = start + i*step
                step = step/10
                print("nokta  ve adım  :" , start , step )
                break
            else :
            
                i = i/2
                x1 = f(start + i*step) 
                i = i*2
                x2 = f(start + i*step)
                i = i*2
                x3 = f(start + i*step)

                print("x1  x2 x3 i:  ",x1,x2,x3,i)
    print("min nokta  :" ,  start)


karar = int(input ("Max için 1 Min için 2 giriniz  :"))

step = float(input ("Enter step size"))

epochs = int(input ("Enter epoch  :"))


start = float(input ("Enter initial value"))

if( karar == 1)  :
    find_max(start,step,epochs)
else :
    find_min(start,step,epochs)  

x = np.arange(-10, 10, 0.001)

plt.plot(x, f(x))
plt.show()