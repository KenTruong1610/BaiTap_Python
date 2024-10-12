"""
Một bạn cần tạo một website yêu cầu người dùng nhập tên người dùng và mật khẩu để đăng ký. Em hãy viết chương trình để kiểm tra tính hợp lệ của mật khẩu mà người dùng nhập vào.
Có 6 tiêu chí kiểm tra mật khẩu bao gồm:
1. Ít nhất 1 chữ cái nằm trong [a-z]
2. Ít nhất 1 số nằm trong [0-9]
3. Ít nhất 1 kí tự nằm trong [A-Z]
4. Ít nhất 1 ký tự nằm trong [$ # @]
5. Độ dài mật khẩu tối thiểu: 6
6. Độ dài mật khẩu tối đa: 30
Chương trình phải chấp nhận một chuỗi mật khẩu phân tách nhau bởi dấu phẩy và kiểm tra xem chúng có đáp ứng những tiêu chí trên hay không. Mật khẩu hợp lệ sẽ được in, mỗi mật khẩu cách nhau bởi dấu phẩy.
"""
import re

def is_valid_password(password):
    if (6 <= len(password) <= 30 and
        re.search("[a-z]", password) and      
        re.search("[0-9]", password) and      
        re.search("[A-Z]", password) and      
        re.search("[$#@]", password) and       
        not re.search("\s", password)):         
    return False

def get_valid_passwords():
    valid_passwords = []  # Danh sách lưu trữ mật khẩu hợp lệ
    while True:
        password = input("Nhập mật khẩu (hoặc gõ 'exit' để thoát): ")
        
        # Kiểm tra điều kiện thoát
        if password.lower() == 'exit':
            break
        
        if is_valid_password(password):
            valid_passwords.append(password)  
            print(f"Mật khẩu hợp lệ: {password}")
        else:
            print("Mật khẩu không hợp lệ. Vui lòng nhập lại.")

    if valid_passwords:
        print("Chuỗi mật khẩu hợp lệ:", ', '.join(valid_passwords))
    else:
        print("Không có mật khẩu hợp lệ.")

get_valid_passwords()
