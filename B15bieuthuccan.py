# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 09:25:54 2024

@author: trankieuvy23717511
"""

import math

a=float(input("nhập vào a: "))
b=float(input("nhập vào b: "))

x1=a**(1/3)
x2=b**(1/3)
y=(a*b)**(1/3)
z=(x1+x2)**2

ketqua=round(((((a+b)/(x1+x2))-y)/(z)),3)

print("Kết quả: ",ketqua)


