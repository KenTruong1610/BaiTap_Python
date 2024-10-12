"""
Bài 26: Viết một chương trình chấp nhận đầu vào là chuỗi các số nhị phân 4 chữ số, phân tách bởi dấu phẩy, kiểm tra xem chúng có chia hết cho 5 không. Sau đó in các số chia hết cho 5 thành dãy phân tách bởi dấu phẩy.
"""
def check_divisible_by_5(binary_numbers):
    value = []
    items = binary_numbers.split(',')
    for p in items:
        decimal_number = int(p, 2)
        if decimal_number % 5 != 0:
            value.append(p)
    return ",".join(value)
binary_numbers = input("Nhập chuỗi các số nhị phân 4 chữ số, phân tách bởi dấu phẩy: ")
print(check_divisible_by_5(binary_numbers))
