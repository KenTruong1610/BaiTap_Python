"""
Một nhà hàng có các món ăn: Gà rán, hamburger, cocacola

Giá của gà rán là: 35.000đ
Giá của hamburger là: 20.000đ
Giá của cocacola là: 12.000đ
Yêu cầu người dùng nhập vào số lượng từng món ăn.

Sau đó in ra hóa đơn theo dạng như sau:

Chào mừng các bạn đến với nhà hàng thức ăn nhanh!
Mời bạn nhập số lượng từng món ăn:

Gà rán: 2
Hamburger: 3
Cocacola: 5

Hóa đơn:
Gà rán             35.000đ x 2
Hamburger          20.000đ x 3
Cocacola           12.000đ x 5

Tổng:
Gà rán             70.000đ
Hamburger          60.000đ
Cocacola           60.000đ
Tổng trước thuế    190.000đ
Thuế(5%)           9.500đ
Tổng sau thuế      195.500đ
"""
def BT47():
    prices = {
        'Gà rán': 35000,
        'Hamburger': 20000,
        'Cocacola': 12000
    }

    print("Chào mừng các bạn đến với nhà hàng thức ăn nhanh!")
    print("Mời bạn nhập số lượng từng món ăn:")
    
    quantities = {}
    for item in prices:
        quantity = int(input(f"{item}: "))  
        quantities[item] = quantity  

    total_before_tax = 0
    bill_details = []  

    for item, price in prices.items():
        item_total = price * quantities[item]
        total_before_tax += item_total
        bill_details.append((item, price, quantities[item], item_total))

    tax_rate = 0.05
    tax = total_before_tax * tax_rate
    total_after_tax = total_before_tax + tax

    print("\nHóa đơn:")
    for item, price, quantity, item_total in bill_details:
        print(f"{item:<20} {price:,}đ x {quantity}") 
    print()  # Dòng trống

    # In tổng
    for item, price, quantity, item_total in bill_details:
        print(f"{item:<20} {item_total:,}đ")
    
    print(f"{'Tổng trước thuế':<20} {total_before_tax:,}đ")
    print(f"{'Thuế(5%)':<20} {tax:,.0f}đ")
    print(f"{'Tổng sau thuế':<20} {total_after_tax:,.0f}đ")

BT47()
