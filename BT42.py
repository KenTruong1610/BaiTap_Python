"""
Bài 42: Viết chương trình nhập ba số a, b, c và thực hiện phép chia c/(a-b). Trong đó, viết code để xử lý trường hợp a-b=0. Sử dụng khối try-catch để xử lý ngoại lệ khi xảy ra tình huống chia cho số 0.
"""
def BT42():
    try:
        a = float(input("Nhập số a: "))
        b = float(input("Nhập số b: "))
        c = float(input("Nhập số c: "))

        difference = a - b

        if difference == 0:
            raise ZeroDivisionError("Phép chia cho số 0 không hợp lệ.")
        
        result = c / difference
        print(f"Kết quả của phép chia c / (a - b) là: {result}")

    except ZeroDivisionError as e:
        print(f"Lỗi: {e}")
    except ValueError:
        print("Vui lòng nhập một số hợp lệ.")

BT42()
