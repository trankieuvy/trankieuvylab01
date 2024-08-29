# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 20:13:28 2024

@author: trankieuvy23717511
"""

print("Bài 10: ")

soxe=int(input("nhập vào số xe của bạn (4 chữ số): "))

soxe1=soxe//1000
soxe2=soxe%1000//100
soxe3=soxe%100//10
soxe4=soxe%10

tong=soxe1+ soxe2+ soxe3+ soxe4
a=tong//10
b=tong%10

c= a + b

d=c//10
e=c%10
print(f"Biển số xe của bạn là: {soxe} và số nút là:{d+e}")

