"""
Bài 50: Nhập vào một chuỗi, hãy đếm xem trong chuỗi có bao nhiêu ký tự in hoa, bao nhiêu ký tự in thường, bao nhiêu ký tự số
"""
def dem_ky_tu(chuoi):
    so_ky_tu_in_hoa = sum(1 for char in chuoi if char.isupper())  
    so_ky_tu_in_thuong = sum(1 for char in chuoi if char.islower())  
    so_ky_tu_so = sum(1 for char in chuoi if char.isdigit()) 

    return so_ky_tu_in_hoa, so_ky_tu_in_thuong, so_ky_tu_so

chuoi_nhap = input("Nhập vào một chuỗi: ")

ky_tu_in_hoa, ky_tu_in_thuong, ky_tu_so = dem_ky_tu(chuoi_nhap)

print(f"Số ký tự in hoa: {ky_tu_in_hoa}")
print(f"Số ký tự in thường: {ky_tu_in_thuong}")
print(f"Số ký tự số: {ky_tu_so}")
