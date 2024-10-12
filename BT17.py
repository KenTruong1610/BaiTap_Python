"""
Bài 19: Viết chương trình chấp nhận một chuỗi số, phân tách bằng dấu phẩy từ giao diện điều khiển, tạo ra một danh sách và một tuple chứa mọi số.
VD: 12,35,56,32,80,9,6,15.
-->['1', '3', '5', '6']
('1', '3', '5', '6')
"""
values=input("Nhập vào các giá trị:")
l=values.split(",")
t=tuple(l)
print (l)
print (t)
