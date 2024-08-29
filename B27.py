# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:18:30 2024

@author: Admin
"""

print("Bài 27: ")

import math

print("Bạn hãy nhập theo quy tắc sau: ")
print("Hình vuông: v","Hình chữ nhật: n", "Hình tròn: t")

a=input("Nhập kí tự theo quy tắc để chọn hình: ")

if a=="v":
    b=int(input("Nhập cạnh hình vuông: "))
    
    C=b**4
    S=b**2
    
    print("Chu vi của hình vuông là:",C,"Diện tích của hình vuông là:",S)   
elif a=="n":
    b=int(input("Nhập chiều rộng hình chữ nhật: "))
    c=int(input("Nhập chiều dài hình chữ nhật: "))
    
    C1=(b+c)*2
    S1=b*c
    
    print("Chu vi hình chữ nhật là:",C1, "Diện tích hình chữ nhật là:",S1)  
elif a=="t":
    r=int(input("Nhập bán kính hình tròn: "))
    C2=2*math.pi*r
    S2=math.pi*r**2
    
    print("Chu vi hình tròn là:",C2,"Diện tích hình tròn là:",S2)
else:
    print("Bạn đã nhập sai theo quy tắc hình")
    
    
    

