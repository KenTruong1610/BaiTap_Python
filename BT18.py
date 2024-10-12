"""
Bài 18: Đầu vào là một mảng số, ví dụ: arr = [1, -2, 3, 4, -9, 6].
Nhiệm vụ là: tìm mảng con liền kề của arr với tổng các item lớn nhất.
Viết hàm getMaxSubSum(arr) sẽ trả về tổng đó.
"""
def getMaxSubSum(arr):
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
