# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:59:27 2024

@author: trankieuvy23717511
"""

print("Bài 8: ")

print("Bạn hãy nhập vào:")
a=int(input("Chiều cao (cm): "))
b=int(input("Cân nặng (kg): "))
a_m=a/100

BMI= b/a_m**2

print("Chỉ số BMI của bạn là: ", round(BMI,1))
if BMI<18.5:
    print("Gầy: Cơ thể thiếu cân, cần tăng cường dinh dưỡng và luyện tập để đạt cân nặng lý tưởng.")
if 18.5 < BMI < 24.9:
    print("Bình thường: Cân nặng phù hợp với chiều cao, bạn đang ở mức lý tưởng.")
if 25<BMI<29.9:
    print("Thừa cân: Cần điều chỉnh chế độ ăn và tăng cường hoạt động thể chất để giảm cân.")  
if BMI>30:
    print("Béo phì: Nguy cơ cao mắc các bệnh liên quan đến béo phì, cần có kế hoạch giảm cân cụ thể và khoa học.")

      



