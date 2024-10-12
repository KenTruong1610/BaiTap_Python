"""
Bài 39:Viết chương trình python để hiển thị thông tin về sinh viên: id, điểm thi hai môn, điểm thể chất, tổng điểm, và điểm trung bình. Tính kế thừa
Dữ liệu:
student_id=1, exam1=7.5, exam2=8.0, physical_score=9.5,
student_id=2, exam1=8.0, exam2=8.0, physical_score=9.0,
student_id=3, exam1=7.0, exam2=8.0, physical_score=10.0

"""
class Student:
    def __init__(self, student_id, exam1, exam2):
        self.student_id = student_id  # ID sinh viên
        self.exam1 = exam1  # Điểm thi môn 1
        self.exam2 = exam2  # Điểm thi môn 2

    def total_score(self):
        """Tính tổng điểm."""
        return self.exam1 + self.exam2

    def average_score(self):
        """Tính điểm trung bình."""
        return self.total_score() / 2.0

    def display_info(self):
        """Hiển thị thông tin sinh viên."""
        print(f"ID: {self.student_id}")
        print(f"Điểm thi môn 1: {self.exam1}")
        print(f"Điểm thi môn 2: {self.exam2}")
        print(f"Tổng điểm: {self.total_score()}")
        print(f"Điểm trung bình: {self.average_score():.2f}")

class PhysicalEducationStudent(Student):
    def __init__(self, student_id, exam1, exam2, physical_score):
        super().__init__(student_id, exam1, exam2)  # Gọi hàm khởi tạo của lớp cha
        self.physical_score = physical_score  # Điểm thể chất

    def total_score(self):
        """Tính tổng điểm bao gồm điểm thể chất."""
        return super().total_score() + self.physical_score

    def average_score(self):
        """Tính điểm trung bình bao gồm điểm thể chất."""
        return self.total_score() / 3.0

    def display_info(self):
        """Hiển thị thông tin sinh viên thể chất."""
        super().display_info()  # Hiển thị thông tin từ lớp cha
        print(f"Điểm thể chất: {self.physical_score}")
        print(f"Tổng điểm (bao gồm điểm thể chất): {self.total_score()}")
        print(f"Điểm trung bình (bao gồm điểm thể chất): {self.average_score():.2f}")

# Dữ liệu sinh viên ban đầu
students = [
    PhysicalEducationStudent(student_id=1, exam1=7.5, exam2=8.0, physical_score=9.5),
    PhysicalEducationStudent(student_id=2, exam1=8.0, exam2=8.0, physical_score=9.0),
    PhysicalEducationStudent(student_id=3, exam1=7.0, exam2=8.0, physical_score=10.0)
]

def display_all_students():
    """Hiển thị thông tin của tất cả sinh viên."""
    for student in students:
        print(f"\nThông tin sinh viên {student.student_id}:")
        student.display_info()

def display_student_by_id(student_id):
    """Hiển thị thông tin của sinh viên theo ID."""
    for student in students:
        if student.student_id == student_id:
            student.display_info()
            return
    print("Không tìm thấy sinh viên với ID đã cho.")

# Menu chính
while True:
    print("\n==========================================================")
    print("MENU")
    print("==========================================================")
    print("1. Quan sát tất cả bản ghi của sinh viên")
    print("2. Quan sát một bản ghi của sinh viên bởi ID")
    print("3. Thoát")
    choice = input("Nhập lựa chọn của bạn (1-3): ")

    if choice == '1':
        display_all_students()
    elif choice == '2':
        try:
            student_id = int(input("Nhập ID sinh viên: "))
            display_student_by_id(student_id)
        except ValueError:
            print("ID không hợp lệ. Vui lòng nhập một số nguyên.")
    elif choice == '3':
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

