#Tính chính xác tuổi của bạn thông qua import datetime
# Tính tuổi dựa trên ngày tháng năm sinh nhập vào
import datetime
a = int(input("Nhập vào ngày sinh của bạn: "))
b = int(input("Nhập vào tháng sinh của bạn: "))
c = int(input("Nhập vào năm sinh của bạn: "))
current_year = datetime.date.today().year
current_month = datetime.date.today().month
current_day = datetime.date.today().day
age_year = current_year - c
age_month = abs(current_month-b)
age_day = abs(current_day-a)
print("Tuổi chính xác của bạn là ", age_day,"ngày" , age_month,"tháng", age_year, "năm tuổi")
