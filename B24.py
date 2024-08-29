# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:44:10 2024

@author: Admin
"""

a=int(input("Nhập số giờ: "))
b=int(input("Nhập số phút: "))
c=int(input("Nhập số giây: "))

if 0<=a<24 and 0<b<60 and 0<c<60:
    print("Thời gian hợp lệ")
else: 
    print("Thời gian không hợp lệ")
    
    