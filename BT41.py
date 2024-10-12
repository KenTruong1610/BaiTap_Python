"""
Bài 41: Sử dụng constructor để tìm số nguyên tố.
"""
class Songuyento:
    def __init__(self, a):
        self.a = a  # Số nguyên cần kiểm tra
        self.k = None  # Biến để lưu kết quả kiểm tra
        self.calculate()  # Gọi hàm calculate để thực hiện kiểm tra

    def calculate(self):
        if self.a < 2:  # Các số < 2 không phải số nguyên tố
            self.k = 0
            return

        # Kiểm tra số nguyên tố
        for i in range(2, self.a // 2 + 1):
            if self.a % i == 0:  # Nếu a chia hết cho i
                self.k = 0  # Không phải số nguyên tố
                return
        self.k = 1  # Là số nguyên tố

    def display(self):
        if self.k == 1:
            print(f"{self.a} là số nguyên tố.")
        else:
            print(f"{self.a} không phải là số nguyên tố.")

# Nhập số nguyên từ người dùng
try:
    number = int(input("Nhập một số nguyên: "))
    songuyento = Songuyento(number)  # Tạo đối tượng của lớp
    songuyento.display()  # Hiển thị kết quả
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")
