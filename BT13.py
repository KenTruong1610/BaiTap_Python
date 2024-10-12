"""
Bài 13: Nhập số tiền lãi qua từng tháng thông qua số tháng, lãi suất và số tiền, từ đó tính tiền qua từng tháng.
"""
a = int (input ("Nhập vào số tháng: "))
b = float (input("Nhập vào lãi suất: "))
c = int (input ("Nhập vào số tiền: "))
for  i in range (1,a + 1):
	lai = ((c*(b/12))/100)
	c += lai
	print (" Tiền lãi tháng", i , "la: ", lai)
	print (" Số tiền tháng" , i , "là: ", c)
