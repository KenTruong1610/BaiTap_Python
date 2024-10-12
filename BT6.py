"""
Bài 6: Viết chương trình tính căn bậc N của 1 số bất kì.
"""
import math
number = float(input("Nhập số cần tính căn bậc n: "))
power = float(input("Nhập số mũ n: "))
result = math.pow(number, 1.0 / power)
print(f"Căn bậc {power} của {number} là {result}")
