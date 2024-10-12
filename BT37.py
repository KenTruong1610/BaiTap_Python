"""
Viết một chương trình C++ để hiển thị một menu cho phép người dùng lựa chọn hoặc quan sát tất cả bản ghi của sinh viên hoặc chỉ quan sát các bản ghi của một sinh viên cụ thể bởi lựa chọn id của sinh viên đó.

==========================================================

MENU
==========================================================

1. Quan sat tat ca ban ghi cua sinh vien

2. Quan sat mot ban ghi cua sinh vien boi ID

3. Hien thi diem thi cuoi ky cao nhat va thap nhat

Nhap lua chon cua ban (1-3): 1

|ID | Kiemtra1 | Kiemtra2 | Giuaky | Cuoiky

| ==================================================

|1232 | 10 | 23 | 45 | 56 |

|2343 | 45 | 43 | 24 | 78 |

|2343 | 34 | 45 | 45 | 45 |

|3423 | 67 | 6 | 65 | 56 |
"""

# Dữ liệu sinh viên mẫu
sinh_vien = [
    {"ID": 1232, "Kiemtra1": 10, "Kiemtra2": 23, "Giuaky": 45, "Cuoiky": 56},
    {"ID": 2343, "Kiemtra1": 45, "Kiemtra2": 43, "Giuaky": 24, "Cuoiky": 78},
    {"ID": 2344, "Kiemtra1": 34, "Kiemtra2": 45, "Giuaky": 45, "Cuoiky": 45},
    {"ID": 3423, "Kiemtra1": 67, "Kiemtra2": 6, "Giuaky": 65, "Cuoiky": 56},
]

def hien_thi_tat_ca_ban_ghi():
    print("| ID  | Kiemtra1 | Kiemtra2 | Giuaky | Cuoiky |")
    print("|" + "=" * 50 + "|")
    for sv in sinh_vien:
        print(f"| {sv['ID']: <4} | {sv['Kiemtra1']: <9} | {sv['Kiemtra2']: <9} | {sv['Giuaky']: <6} | {sv['Cuoiky']: <6} |")
    print("|" + "=" * 50 + "|")

def hien_thi_ban_ghi_theo_id(id_sv):
    for sv in sinh_vien:
        if sv['ID'] == id_sv:
            print("| ID  | Kiemtra1 | Kiemtra2 | Giuaky | Cuoiky |")
            print("|" + "=" * 50 + "|")
            print(f"| {sv['ID']: <4} | {sv['Kiemtra1']: <9} | {sv['Kiemtra2']: <9} | {sv['Giuaky']: <6} | {sv['Cuoiky']: <6} |")
            print("|" + "=" * 50 + "|")
            return
    print("Không tìm thấy sinh viên với ID:", id_sv)

def hien_thi_diem_cuoiky_cao_nhat_thap_nhat():
    cuoiky_diem = [sv['Cuoiky'] for sv in sinh_vien]
    print(f"Điểm thi cuối kỳ cao nhất: {max(cuoiky_diem)}")
    print(f"Điểm thi cuối kỳ thấp nhất: {min(cuoiky_diem)}")

def main():
    while True:
        print("==========================================================")
        print("MENU")
        print("==========================================================")
        print("1. Quan sat tat ca ban ghi cua sinh vien")
        print("2. Quan sat mot ban ghi cua sinh vien boi ID")
        print("3. Hien thi diem thi cuoi ky cao nhat va thap nhat")
        print("4. Thoat")
        lua_chon = input("Nhap lua chon cua ban (1-4): ")

        if lua_chon == '1':
            hien_thi_tat_ca_ban_ghi()
        elif lua_chon == '2':
            id_sv = int(input("Nhap ID cua sinh vien: "))
            hien_thi_ban_ghi_theo_id(id_sv)
        elif lua_chon == '3':
            hien_thi_diem_cuoiky_cao_nhat_thap_nhat()
        elif lua_chon == '4':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại.")

if __name__ == "__main__":
    main()
