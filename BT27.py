"""
Bài 27: Nhập tên các con vật rồi sắp xếp chúng theo Alphabet chữ cái đầu của mỗi từ.
"""
Ten = input("Nhập tên các con vật, phân tách bởi dấu phẩy: ")
Ten_list = Ten.split(",")
Ten_list.sort(key=lambda x: x.split()[0])
print("Các con vật theo thứ tự Alphabet chữ cái đầu tiên của mỗi từ là: ")
for name in Ten_list:
    print(name)
