"""
Bài 44: Viết một hàm để tính giai thừa của một số nguyên dương.
"""
def tinh_giai_thua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * tinh_giai_thua(n-1)

so_nguyen = int(input("Nhập một số nguyên dương: "))

while so_nguyen < 0:
    so_nguyen = int(input("Vui lòng nhập một số nguyên dương: "))

ket_qua = tinh_giai_thua(so_nguyen)

print(f"Giai thừa của {so_nguyen} là {ket_qua}")