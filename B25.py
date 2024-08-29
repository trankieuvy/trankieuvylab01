# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:25:45 2024

@author: trankieuvy23717511

"""
a=input("Nhập một chữ cái bất kì: ")
if a.islower():
    a=a.upper()
    print(a)
elif a.isupper():
    a=a.lower()
    print(a)
    
    
