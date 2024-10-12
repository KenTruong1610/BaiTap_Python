"""
Bài 30: Một dạng list chạy d.sách mảng 2 chiều gồm có món đồ cần mua và giá như sau:
Chuối	5.000	2023-05-01
Xoài	20.000	2023-05-06
Táo	15.000	2023-06-03
Đu đủ	25.000	2023-08-04
Ổi	15.000	2023-09-12
 Từ đó người dùng nhập món đồ cần mua và số lượng mua món hàng đó, từ món hàng trên hãy tính tổng số lượng món đã mua và tính tổng tất cả món hàng đã nhập dựa trên số lượng.
"""
items = [
    ["Chuối", 5000, "2023-05-01"],
    ["Xoài", 20000, "2023-05-06"],
    ["Táo", 15000, "2023-06-03"],
    ["Đu đủ", 25000, "2023-08-04"],
    ["Ổi", 15000, "2023-09-12"]
]
total_quantity = 0
total_price = 0
while True:
    item_name = input("Nhập tên món hàng (nhập 'x' để kết thúc): ")
    if item_name == 'x':
        break
    quantity = int(input("Nhập số lượng cần mua: "))
    for item in items:
        if item[0] == item_name:
            print("Ngày nhập: ",item[2], ",Giá tiền: ",item[1], "đồng.")
            total_quantity += quantity
            total_price += quantity * item[1]
print("Tổng số lượng của các món hàng đã nhập là: ",total_quantity)
print("Tổng giá trị của các món hàng đã nhập là: " ,total_price, "đồng.")
