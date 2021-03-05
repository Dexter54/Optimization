import matplotlib.pyplot as plt
import numpy as np
import pandas

from math import exp, expm1,sin,atan,radians



def f(x):
    #return pow(x,2) + 10*np.sin(x)
    return 0.65 - (0.75/(1 + x*x)) - 0.65*x*np.arctan(1/x)

def der_f(x):
    return 2*x + 10*np.cos(x)



def find_max(x1,x2,x3,x4,step1,step2,hata,epoch)  :

    print("alfa1  :",step1)
    print("alfa2  :",step2)

    hata2 = 10
    i = 0
    while i<epoch and hata2>hata :

        x3 = step2*x1 + step1*x2
        x4 = step1*x1 + step2*x2

        f1 = f(x1)   
        f3 = f(x3)
        f4 = f(x4)
        f2 = f(x2)

        hata2 = abs(x1 - x2)

        print("iterasyon  :",i+1)
        print("hata  :",hata2)
        print("x1  :",x1)
        print("x2  :",x2)
        print("x3  :",x3)
        print("x4  :",x4)
        print("  ")
        print("f(x1)  :",f1)        
        print("f(x2)  :",f2)        
        print("f(x3)  :",f3)        
        print("f(x4)  :",f4)
        print("  ")
        print("  ")
        print("  ")

        if(f3 >= f4) :
            x2 = x4
        else :
            x1 = x3
               
        i = i+1


    
    f1 = f(x1)   
    f3 = f(x3)
    f4 = f(x4)
    f2 = f(x2)
    if(f3 >= f4 ) :
        if( f3 > f1 and f3 > f2) :
            print("max. nokta  :",x3)
            print("iterasyon sayısı  :",i)
            print("hata  :",hata2)
        else :
            print("max nokta bulunamadı.")
            print("iterasyon sayısı  :",i)
            print("hata  :",hata2)
    else :
        if( f4 > f1 and f4 > f2) :
            print("max. nokta  :",x4)
            print("iterasyon sayısı  :",i)
            print("hata  :",hata2)
        else :
            print("max nokta bulunamadı.")
            print("iterasyon sayısı  :",i)
            print("hata  :",hata2)

        
        
       


def find_min(x1,x2,x3,x4,step1,step2,hata,epoch)  :
    
    print("alfa1  :",step1)
    print("alfa2  :",step2)
    hata2 = 10
    i = 0
    while i<epoch and hata2>hata :

        x3 = step2*x1 + step1*x2
        x4 = step1*x1 + step2*x2

        f1 = f(x1)   
        f3 = f(x3)
        f4 = f(x4)
        f2 = f(x2)

        hata2 = abs(x1 - x2)
        
        print("iterasyon  :",i+1)
        print("hata  :",hata2)
        print("x1  :",x1)
        print("x2  :",x2)
        print("x3  :",x3)
        print("x4  :",x4)
        print("  ")
        print("f(x1)  :",f1)        
        print("f(x2)  :",f2)        
        print("f(x3)  :",f3)        
        print("f(x4)  :",f4)
        print("  ")
        print("  ")
        print("  ")

        if(f3 <= f4) :
            x2 = x4
        else :
            x1 = x3

        i = i+1

    
    f1 = f(x1)   
    f3 = f(x3)
    f4 = f(x4)
    f2 = f(x2)
    if(f3 <= f4 ) :
        if( f3 < f1 and f3 < f2) :
            print("min. nokta  :",x3)
            print("iterasyon sayısı  :",i)
            print("hata  :",hata2)
        else :
            print("min nokta bulunamadı.")
            print("iterasyon sayısı  :",i)
            print("hata  :",hata2)
    else :
        if( f4 < f1 and f4 < f2) :
            print("min. nokta  :",x4)
            print("iterasyon sayısı  :",i)
            print("hata  :",hata2)
        else :
            print("min nokta bulunamadı.")
            print("iterasyon sayısı  :",i)
            print("hata  :",hata2)



karar = float(input ("Max için 1 , min için 2 giriniz"))

step1 = 0.382
step2 = 1 - 0.382

hata = float(input ("Hata miktarı giriniz  :"))
epoch = float(input ("Epoch  miktarı giriniz  :"))

x1 = float(input ("x1 noktasını giriniz  :"))
x2 = float(input ("x2 noktasını giriniz  :"))

x3 = 0
x4 = 0


if(karar == 1) :
    find_max(x1,x2,x3,x4,step1,step2,hata,epoch)
else :
    find_min(x1,x2,x3,x4,step1,step2,hata,epoch)

x = np.arange(-10, 10, 0.001)

print(sin(radians(30)))
plt.plot(x, f(x))
plt.show()