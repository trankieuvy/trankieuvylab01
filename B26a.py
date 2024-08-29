# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:51:26 2024

@author: trankieuvy23717511
"""
print("Bài 26a: ")

a=float(input("Nhập số a: "))
b=float(input("Nhập số b: "))
c=float(input("Nhập số c: "))

if a>b:
    a, b=b, a
if a>c:
    a, c=c, a
if b>c:
    b, c=c, b

print("Các sóo được sắp xếp theo thứ tự tăng dần là: ", a,b,c)

