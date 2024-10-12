"""
Bài 21: Viết một chương trình có hộp dữ liệu có nhiều keyword. Sắp xếp các số theo giá trị nhỏ dần
"""
participant_list = [
    ('Lê An', 50, 18),
    ('Trần Bình', 75, 12),
    ('Trần Tâm', 75, 20),
    ('Thanh Lam', 90, 22),
    ('Vũ Lan', 45, 12)
]
sorted_list = sorted(participant_list, key=lambda item: (100-item[1], item[2]))
print(sorted_list)
