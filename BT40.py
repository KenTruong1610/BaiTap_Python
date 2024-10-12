"""
Bài 40: Tạo giao diện calendar
"""
import tkinter as tk
from tkinter import messagebox
import calendar
from tkcalendar import Calendar

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lịch")
        self.root.geometry("400x400")

        # Thêm tiêu đề
        self.title_label = tk.Label(root, text="LỊCH", font=("Arial", 16))
        self.title_label.pack(pady=10)

        # Tạo lịch
        self.calendar = Calendar(root, selectmode='day', year=2024, month=10, day=13)
        self.calendar.pack(pady=20)

       
if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
