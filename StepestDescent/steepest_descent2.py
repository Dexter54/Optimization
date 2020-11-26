import matplotlib.pyplot as plt
import numpy as np

from math import exp, expm1,sin,atan,radians,ceil



def f(x1,x2,x3):

    return x1*x1 + x2*x2 + 4*(x1-x2+x3-1)*(x1-x2+x3-1)

def der_f1(x1,x2,x3):

    return 2*x1 + 8*(x1-x2+x3-1)

def der_f2(x1,x2,x3):

    return 2*x2 -8*(x1-x2+x3-1)

def der_f3(x1,x2,x3):

    return 8*(x1-x2+x3-1)



def golden_section(x1,x2,Value1,Value2,Value3,Deriv1,Deriv2,Deriv3) :


    step1 = 0.382
    step2 = 1 - 0.382

    hata2 = 10
    i = 0
    while hata2>0.00001 :

        x3 = step2*x1 + step1*x2
        x4 = step1*x1 + step2*x2

        f1 = f((Value1+x1*Deriv1),(Value2+x1*Deriv2),(Value3+x1*Deriv3))   
        f3 = f((Value1+x3*Deriv1),(Value2+x3*Deriv2),(Value3+x3*Deriv3)) 
        f4 = f((Value1+x4*Deriv1),(Value2+x4*Deriv2),(Value3+x4*Deriv3)) 
        f2 = f((Value1+x2*Deriv1),(Value2+x2*Deriv2),(Value3+x2*Deriv3)) 

        hata2 = abs(x1 - x2)

        if(f3 <= f4) :
            x2 = x4
        else :
            x1 = x3
               
        i = i+1


    
    f1 = f((Value1+x1*Deriv1),(Value2+x1*Deriv2),(Value3+x1*Deriv3))   
    f3 = f((Value1+x3*Deriv1),(Value2+x3*Deriv2),(Value3+x3*Deriv3)) 
    f4 = f((Value1+x4*Deriv1),(Value2+x4*Deriv2),(Value3+x4*Deriv3)) 
    f2 = f((Value1+x2*Deriv1),(Value2+x2*Deriv2),(Value3+x2*Deriv3)) 

    if(f3 <= f4 ) :
        if( f3 < f1 and f3 < f2) :

            return x3
        else :
            print("min nokta bulunamadı.")
            #print("iterasyon sayısı  :",i)
            #print("hata  :",hata2)
  
    else :
        if( f4 < f1 and f4 < f2) :

            return x4
        else :
            print("min nokta bulunamadı.")
            #print("iterasyon sayısı  :",i)
            #print("hata  :",hata2)


        

Value1 = -1
Value2 = -1
Value3 = -1
hata = 0.01

#Start = 0
#End = 20

gb = -5
gs =  5

f_ilk = f(Value1,Value2,Value3)

print("ilk hesap :",f_ilk)

Deriv1 = -1*der_f1(Value1,Value2,Value3)
Deriv2 = -1*der_f2(Value1,Value2,Value3)
Deriv3 = -1*der_f3(Value1,Value2,Value3)

step = golden_section(gb,gs,Value1,Value2,Value3,Deriv1,Deriv2,Deriv3)
print("step  :",step)
Value1 = Value1 + step*Deriv1 
Value2 = Value2 + step*Deriv2 
Value3 = Value3 + step*Deriv3 

f_son = f(Value1,Value2,Value3)
print("son hesap :",f_son)

counter = 0

temp = f_son - f_ilk


while counter < 150 and abs(f_son - f_ilk) > 0.00000001 :

    print("iterasyon  :", counter + 1)

    f_ilk = f_son

    Deriv1 = der_f1(Value1,Value2,Value3)
    Deriv2 = der_f2(Value1,Value2,Value3)
    Deriv3 = der_f3(Value1,Value2,Value3)

    #print("Türev1 :",Deriv1) 
    #print("Türev2 :",Deriv2)
    #print("Türev3 :",Deriv3)

    step = golden_section(gb,gs,Value1,Value2,Value3,Deriv1,Deriv2,Deriv3)
    #print("step  :",step)
    Value1 = Value1 + step*Deriv1 
    Value2 = Value2 + step*Deriv2 
    Value3 = Value3 + step*Deriv3 


    
    print("Nokta1 :",Value1) 
    print("Nokta2 :",Value2)
    print("Nokta3 :",Value3)


    f_son = f(Value1,Value2,Value3)


    #print("hata toleransı",abs(f_son - f_ilk))
    print("******************")
    print("******************") 
    print("******************")

    counter = counter + 1
     

#print("Nokta1 :",ceil(Value1)) 
#print("Nokta2 :",ceil(Value2))
#print("Nokta3 :",ceil(Value3))
print("F değeri :",f_son)
#print("ilk değişim : ",temp)