"""
Bài 14: Nhập n để tính tổng dãy số đã cho: S = 1 + 2 + 3 + …. + n
"""
n = int(input("Nhập số nguyên dương n: "))
s = 0
i = 1
while i <= n :
	s+= i;
	i+=1;
print("Tổng dãy số từ 1 đến", n," là:", s)
