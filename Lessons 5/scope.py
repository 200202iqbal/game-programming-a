i = 5

def f(arg=i):
    print(arg)

i = 6
f()#hasilnya 5 karena i sebelumnya dideklarasikan sebagai 5
#f(i) hasilnya akan 6, karena nilai i sudah dirubah menjadi 6