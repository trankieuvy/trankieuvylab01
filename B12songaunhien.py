# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 20:48:09 2024

@author: trankieuvy23717511
"""

print("Bài 12: ")
import random
print("a. Từ 0 đến 100")
#từ 0 đến 100
songuyen=random.randint(0,100)
print("Số nguyên ngẫu nhiên:",songuyen)

sothuc=random.uniform(0,100)
print("Số thực ngẫu nhiên:",round(sothuc,2))

#từ 50 đến 99
print("b. Từ 50 đến 99")
songuyenb=random.randint(50, 99)
sothucb=random.uniform(50,99)
print("Số nguyên ngẫu nhiên:",songuyenb)
print("Số thực ngẫu nhiên:",round(sothucb,2))

#từ -39 đến 79
print("c. Từ -39 đến 79")
songuyenc=random.randint(-39,79)
sothucc=random.uniform(-39,79)
print("Số nguyên ngẫu nhiên:",songuyenc)
print("Số thực ngẫu nhiên:",round(sothucc,2))

#từ -79 đến -39
print("d. Từ -79 đến -39")
songuyend=random.randint(-79,-39)
sothucd=random.uniform(-79,-39)
print("Số nguyên ngâu nhiên:", songuyend)
print("Số thực ngẫu nhiên:",round(sothucd,2))


      
      
