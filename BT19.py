"""
Bài 19: Bạn có một mảng các đối tượng người dùng, mỗi đối tượng có user.name. Viết code chuyển đổi nó thành một mảng tên.
"""
users = [
    {'name': 'John'},
    {'name': 'Alice'},
    {'name': 'Bob'}
]

names = [user['name'] for user in users]

print(names)  
