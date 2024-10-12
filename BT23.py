"""
Bài 23: Viết chương trình nhập vào 1 dãy số nguyên (n: nhập vào). Viết chương trình KT số hoàn hảo trong dãy vừa nhập.
"""
n = int(input("Nhập số nguyên: "))
tong = 0
for i in range(1, n):
    if (n % i == 0):
        tong += i
if (tong == n):
    print(n, "là số hoàn hảo")
else:
    print(n, "không phải là số hoàn hảo")
