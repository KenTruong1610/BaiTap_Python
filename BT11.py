"""
Bài 11: Viết chương trình tính chu vi, diện tích tam giác a,b,c (với a,b,c>0) (Có thể có or không)
"""
import math
a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
c = float(input("Nhập giá trị c: "))
if (a+b>c) and (b+c>a) and (c+a>b):
    print("Tạo thành tam giác")
    CV = (a+b+c)
    print("Chu vi hình tam giác : ", CV)
    p = (a+b+c)/2
    DT = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("Diện tích tam giác là: ", DT)
else:
    print("Không tạo thành tam giác")
