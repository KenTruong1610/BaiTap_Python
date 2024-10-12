"""
Bài 25: Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 3, nằm trong đoạn 1000 và 2400 (tính cả 1000 và 2400). Các số thu được sẽ được in thành chuỗi trên một dòng, cách nhau bằng dấu phẩy.
"""
j=[]
for i in range(1000, 2401):
    if (i%7==0) and (i%3!=0):
        j.append(str(i))
print (','.join(j))
