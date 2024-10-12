"""
Bài 29: Lập list để tạo ra dãy fibonacci.
VD: Nhập số: 5        KQ: [1;1;2;3;5]
"""
def fibonacci():
    num = int(input("How many numbers that generates?: "))
    i = 1
    if num < 0:
        print("Please enter a non-negative number.")
        exit(0)
    elif num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    else:
        fib = [1,1]
        while i < (num - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib
print(fibonacci())
input()
