"""
Bài 34: Cho khối lượng của các quả cân đang có là
[1, 2, 4, 8, 16, 32, 64, 128, 256]
Người dùng sẽ nhập khối lượng của vật M.
Hệ thống sẽ tính toán các quả cân sẽ được sử dụng.
*Lưu ý: M chỉ được nhập khi không quá 512.
"""
def tinh_cac_qua_can(m, quacan):
    print(f"Trọng lượng của vật M là: {m}g")
    print("Các quả cân có thể sử dụng để cân vật M:")
    for weight in reversed(quacan):
        if m >= weight:
            print(f"Sử dụng quả cân {weight}g")
            m -= weight

def BT34():
    quacan = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    while True:
        m = int(input("Nhập trọng lượng của vật M (M < 512g): "))
        if m >= 512 or m < 0:
            print("Trọng lượng của vật không hợp lệ. Hãy nhập lại.")
        else:
            break  
    tinh_cac_qua_can(m, quacan)


BT34()
