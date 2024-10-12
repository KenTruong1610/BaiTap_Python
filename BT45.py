"""
Bài 45: Viết một chương trình để tìm số lớn nhất trong một danh sách số nguyên, nhưng không vượt quá một giới hạn được chỉ định.
"""

def tim_so_lon_nhat(danh_sach, gioi_han):
    so_lon_nhat = float('-inf')  
    for so in danh_sach:
        if so > so_lon_nhat and so <= gioi_han:
            so_lon_nhat = so

    if so_lon_nhat == float('-inf'):
        return None  
    return so_lon_nhat

danh_sach_so = [10, 25, 15, 30, 5, 20]
gioi_han = 25

ket_qua = tim_so_lon_nhat(danh_sach_so, gioi_han)

if ket_qua is not None:
    print(f"Số lớn nhất không vượt quá giới hạn {gioi_han} là: {ket_qua}")
else:
    print("Không có số nào thỏa mãn điều kiện.")
