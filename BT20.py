"""
Bài 20: Viết chương trình sắp xếp các chữ cái trong tệp. VD: abcdefg
"""
def sort_letters():
    input_string = input("Nhập chuỗi các chữ cái (ví dụ: abcdefg): ")
    letters = [char for char in input_string if char.isalpha()]
    sorted_letters = sorted(letters)
    print("Chữ cái đã được sắp xếp:", ''.join(sorted_letters))
sort_letters()

