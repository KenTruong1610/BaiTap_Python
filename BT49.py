"""
Cho một chuỗi ký tự S (gồm chữ và số). Hãy viết chương trình tách chữ và số thành hai chuỗi riêng biệt.
File chuoi.inp chứa duy nhất 1 chuỗi S
Hãy tách và ghi vào file chuoi.out 2 dòng, dòng thứ nhất ghi chuỗi ký tự chữ, dòng thứ hai ghi chuỗi ký tự số.
Nếu như chuỗi nào rỗng thì ghi dấu trừ ‘-’.
VD:
chuoi.inp   chuoi.out
a1B2c34d    aBcd
            1234
"""
def tach_chu_so(filename_in, filename_out):
    with open(filename_in, 'r') as file:
        chuoi = file.readline().strip()

    chuoi_chu = ''.join([char for char in chuoi if char.isalpha()])  
    chuoi_so = ''.join([char for char in chuoi if char.isdigit()])    

    if not chuoi_chu:
        chuoi_chu = '-'
    if not chuoi_so:
        chuoi_so = '-'

    with open(filename_out, 'w') as file:
        file.write(chuoi_chu + '\n')
        file.write(chuoi_so + '\n')

tach_chu_so('chuoi.inp', 'chuoi.out')
