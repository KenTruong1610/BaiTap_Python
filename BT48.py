"""
Bài 48: Viết hàm có tham số đầu vào là một dictionary, hãy tạo một dictionary mới hoán đổi giá trị và key của dictionary đầu vào, rồi trả về dicionary mới đó. Nếu sau khi hoán đổi có 2 key trùng nhau (do dictionary đầu vào có 2 giá trị trùng nhau), hàm trả về None
"""
def swap_dict(input_dict):
    swapped_dict = {}

    for key, value in input_dict.items():
        if value in swapped_dict:
            return None  
        swapped_dict[value] = key  

    return swapped_dict  

def BT48():
    input_dict = {}
    n = int(input("Nhập số lượng phần tử trong dictionary: "))
    
    for _ in range(n):
        key = input("Nhập key: ")
        value = input("Nhập value: ")
        input_dict[key] = value

    print("Dictionary ban đầu:", input_dict)

    result = swap_dict(input_dict)
    if result is not None:
        print("Dictionary hoán đổi:", result)
    else:
        print("Có giá trị trùng lặp, không thể hoán đổi.")

if __name__ == "__main__":
    BT48()
