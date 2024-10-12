"""
Bài 8: Cho các số thực A, B, C và D. Bạn hãy tính tích của 4 số để biết đó là số âm, số dương hay bằng 0.
* Lưu ý: 1 là số dương, 0 là bằng 0 và – 1 là số âm.
"""
a = float(input('Nhập só thực A: '))
b = float(input('Nhập số thực B: '))
c = float(input('Nhập số thực C: '))
d = float(input('Nhập số thực D: '))
Tich = a * b * c * d 
if (a == 0) or (b == 0) or (c == 0) or (d == 0) :
	print (0)
elif Tich > 0:
	print(1)
else: 
	print(-1)
