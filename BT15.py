"""
Bài 15: Tính chuỗi dãy số sau: S = 1+ 1/2+1/3+⋯+1/n  
"""
n = int(input("Nhập vào số n: "))
sum = 0
for i in range (1, n+1):
	sum += 1/i
print ("Tổng của 1 + 1/2 + 1/3 + .... + 1/n là: ", sum)
