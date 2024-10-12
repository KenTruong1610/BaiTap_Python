"""
Bài 16: Nhập các số cần thiết để nhập các giá trị của phương trình ax + b (Có sử dụng khai báo hàm def)
"""
def TOAN(a,b):
	while True:
		x = float(input("Nhập giá trị của x (nhập -1 để kết thúc): "))
		if x == -1:
			break
		result = a * x + b
		print("Kết quả của phương trình" ,a,"x +",b, "là: ", result)
a = float(input("Nhập giá trị của a: "))
b = float(input("Nhập giá trị của b: "))
TOAN(a,b)
