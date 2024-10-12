"""
BT36: Cho 5 dữ liệu được nhập từ người dùng gồm: Tên, Năm sinh, Điểm và xếp loại.
Tạo 1 chương trình có định dạng sau:
BẢNG ĐIỂM TỐT NGHIỆP
Cấp cho sinh viên {Tên}, năm sinh {Năm Sinh}.
Trong kì thì tốt nghiệp 2021, sinh viên trên đã đạt điểm trung bình là {Điểm}, và được xếp loại {xếp loại}.
Sinh viên có thứ hạng .... trong lớp.
Hãy tính toán thứ hạng trong lớp (theo xếp loại trước và điểm sau) và in theo mẫu.


"""
def sap_xep_thu_hang(data):
    xep_loai_thu_tu = {
        "Giỏi": 1,
        "Khá": 2,
        "Trung bình": 3
    }
    
    data.sort(key=lambda sv: (xep_loai_thu_tu[sv[3]],float(sv[2])))
    data.reverse()

def BT36():
    n = 5 
    thong_tin_sv = []

    for i in range(n):
        print(f"Nhập thông tin của sinh viên thứ {i + 1}:")
        ho_ten = input("Họ và tên: ")
        nam_sinh = input("Năm sinh: ")
        diem_trung_binh = input("Điểm trung bình: ")
        xep_loai = input("Xếp loại (Giỏi/Khá/Trung bình): ")
        thong_tin_sv.append([ho_ten, nam_sinh, diem_trung_binh, xep_loai])

    sap_xep_thu_hang(thong_tin_sv)

    print("------------------------")

    for i in range(n):
        print("\nBẢNG ĐIỂM TỐT NGHIỆP")
        print(f"Cấp cho sinh viên {thong_tin_sv[i][0]}, năm sinh {thong_tin_sv[i][1]}.")
        print(f"Trong kì thì tốt nghiệp 2021, sinh viên trên đã đạt điểm trung bình là {thong_tin_sv[i][2]}, và được xếp loại {thong_tin_sv[i][3]}.")
        print(f"Sinh viên có thứ hạng {i + 1} trong lớp\n")
        print("------------------------")


BT36()
