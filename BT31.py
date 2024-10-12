"""
Bài 31: Cho ba số a, b, c là các số tự nhiên, hãy dùng vòng lặp để tìm các ước chung của nó.
Yêu cầu:
1. Tính tổng các ước chung của cả 3 số.
2. Xem thử tổng đó có chia hết cho 2 không?
"""
a = int(input("Nhập số tự nhiên thứ nhất: "))
b = int(input("Nhập số tự nhiên thứ hai: "))
c = int(input("Nhập số tự nhiên thứ ba: "))
UC = 1
for i in range(1, int(min(a, b, c))+1):
    if a % i == 0 and b % i == 0 and c % i == 0:
        UC = i
Sum = sum(set([i for i in range(1, int(max(a, b, c))+1) if a % i == 0 and b % i == 0 and c % i == 0]))
if Sum % 2 == 0:
    print("Tổng các ước của " ,a,"",b, "và" ,c, "là" ,Sum, "và chia hết cho 2.")
else:
    print("Tổng các ước của " ,a,"",b, "và" ,c, "là" ,Sum, "và không chia hết cho 2.")
