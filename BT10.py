"""
Bài 10: Nhập tên và số tiền của nhân viên đi làm theo tháng, biết:
"""
Nếu đi làm dưới 2 tháng trong năm: 500000 VND
Nếu đi làm trên 2 tháng trong năm: Số tháng x 250000VND
a = input ("Nhập tên của nhân viên: ")
b = int (input("Nhập số tháng đi làm: "))
if b <= 2 :
	print ("Tiền lương của", a , "là: 500000VND" )
else:
	x1 = b * 250000
	print ("Tiền lương của", a , "là:", x1, "VND")
