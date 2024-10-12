"""
Bài 2: Viết một chương trình tính giá trị của 
a+ab+abc+abcd với a,b,c,d là số được nhập vào bởi 
người dùng.
"""
a = input("Nhập số a: ")
b = input("Nhập số b: ")
c = input("Nhập số c: ")
d = input("Nhập số d: ")
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,b) )
n3 = int( "%s%s%s" % (a,b,c) )
n4 = int( "%s%s%s%s" % (a,b,c,d) )
print ("Tổng là: ",n1+n2+n3+n4)
