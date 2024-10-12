"""
Bài 43: Viết một chương trình chuyển đổi nhiệt độ từ độ C sang độ F hoặc ngược lại, dựa vào lựa chọn của người dùng.
"""
def BT43():
    print("Chương trình chuyển đổi nhiệt độ")
    print("1. Chuyển đổi từ độ C sang độ F")
    print("2. Chuyển đổi từ độ F sang độ C")
    lua_chon = input("Nhập lựa chọn của bạn (1 hoặc 2): ")

    if lua_chon == '1':
        do_c = float(input("Nhập nhiệt độ trong độ C: "))  # Sửa lỗi cú pháp ở đây

        do_f = (do_c * 9/5) + 32

        print(f"{do_c} độ C = {do_f} độ F")

    elif lua_chon == '2':
        do_f = float(input("Nhập nhiệt độ trong độ F: "))

        do_c = (do_f - 32) * 5/9  # Sửa dấu '–' thành '-'

        print(f"{do_f} độ F = {do_c} độ C")

    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn 1 hoặc 2.")

# Gọi hàm để thực thi chương trình
BT43()
