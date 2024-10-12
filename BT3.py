"""
Viết hàm tính âm lịch với số dương lịch cho trước? VD: Namam(2022) => Nhâm Dần
"""
can = ['Canh', 'Tân', 'Nhâm', 'Quý','Giáp', 'Ất', 'Bính', 'Đinh','Mậu','Kỷ']
chi = ['Thân', 'Dậu', 'Tuất', 'Hợi','Tí','Sửu','Dần', 'Mão', 'Thìn', 'Tị', 'Ngọ', "Mùi"]
nam = int(input("Nhap vao nam: "))
vitri_can = nam%10
vitri_chi = nam%12
print(can[vitri_can]+" " +chi[vitri_chi])
