"""
Bài 12: Viết chương trình vẽ một tam giác vuông cân
có dạng như sau:
*
**
***
****
*****
******
"""
n = 6;
print("Ve tam giac sao vuong can: ")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end = " ");
    print()
