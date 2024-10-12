"""
Bài 35: Hệ phương trình gồm 2 phương trình, 3 hệ số.
"""
def main():

    a1 = float(input("Nhập a1: "))
    b1 = float(input("Nhập b1: "))
    c1 = float(input("Nhập c1: "))
    a2 = float(input("Nhập a2: "))
    b2 = float(input("Nhập b2: "))
    c2 = float(input("Nhập c2: "))
    
    d = a1 * b2 - a2 * b1
    dx = c1 * b2 - c2 * b1
    dy = a1 * c2 - a2 * c1
    
    if d != 0:
        x = dx / d
        y = dy / d
        print(f"Hệ có một nghiệm: x={x}, y={y}")
    elif d == 0 and dx != 0:
        print("Hệ phương trình vô nghiệm")
    elif d == 0 and dx == 0:
        print("Hệ phương trình có vô số nghiệm")

main()
