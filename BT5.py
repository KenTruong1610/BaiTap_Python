"""
Bài 5: Nhập dữ liệu trên hệ thống  mức lương tối thiểu của công ty trả cho nhân viên, từ đó biết được lương của nhân viên: 
Biết:
     - Tổng giám đốc : Mức lương tối thiểu x 2.14
     - Phó giám đốc: Mức lương tối thiểu x 2.03
     - Quản lý: Mức lương tối thiểu x 1.82
     - Còn lại Mức lương tối thiểu x 1.56
"""
total_salary = float(input("Nhập mức lương tối thiểu của công ty: "))
CEO_salary = total_salary * 2.14
Deputy_CEO_salary = total_salary * 2.03
Manager_salary = total_salary * 1.82
Other_salary = total_salary * 1.56

print("Mức lương của Tổng giám đốc là: ", CEO_salary)
print("Mức lương của Phó giám đốc là: ", Deputy_CEO_salary)
print("Mức lương của Quản lý là: ", Manager_salary)
print("Mức lương của nhân viên còn lại là: ", Other_salary)
