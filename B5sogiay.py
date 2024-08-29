# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:10:28 2024

@author: trankieuvy23717511
"""

print("Bài 5: ")
a =int(input("nhập vào số giờ: "))
b =int(input("nhập vào số phút: "))
c =int(input("nhập vào số giây: "))

print("thời gian đã được nhập:{}hh:{}mm:{}ss ".format(a,b,c))

sogiay= a*3600 + b*60 +c

print("số giây được quy đổi : ", sogiay)
