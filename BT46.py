"""
Phỏng đoán COLLATZ
Giả sử ta có một số n
Phỏng đoán COLLATZ hoạt động như sau:
Nếu n là số chẵn, thì ta chia n cho 2 (n/2)
Nếu n là số lẻ, thì ta nhân n cho 3 rồi + 1 (3n + 1)
Phỏng đoán hoạt động cho đến khi nào n = 1
Yêu cầu:
Nhập vào số nguyên dương m, hãy in ra dãy phỏng đoán COLLATZ từ 1 đến m (mỗi một phỏng đoán ta in trên 1 dòng, mỗi một số cách nhau một dấu phẩy)
Ví dụ:
Nhập: m = 6
In ra:
1 
2,1 
3,10,5,16,8,4,2,1 
4,2,1 
5,16,8,4,2,1 
6,3,10,5,16,8,4,2,1 
"""
def collatz_sequence(n):
    sequence = []  
    while n != 1:  
        sequence.append(n) 
        if n % 2 == 0:  
            n = n // 2  
        else:  
            n = 3 * n + 1  
    sequence.append(1) 
    return sequence

def main():
    m = int(input("Nhập số nguyên dương m: "))  
    for i in range(1, m + 1): 
        seq = collatz_sequence(i)  
        print(",".join(map(str, seq)))  

if __name__ == "__main__":
    main()
