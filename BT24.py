"""
Câu 24: Dưới dạng class có 2 kiểu dữ liệu là tên và lớp. Từ nguồn dữ liệu ban đầu là ‘An’ và ‘12’ hãy nhập dữ liệu và điền thông tin của chúng.
"""
class AB:
	def __init__ (self, aten,alop):
		self.ten = aten
		self.lop = alop
AB_A = AB('An','12')
print('Ten cua A la: ', AB_A.ten)
print('Lop: ', AB_A.lop)
