# fungsi python yang berisi yield berarti fungsi generator
# keyword return digunakan untuk membalikan nilai
# keyword yield digunakan juga untuk membalikkan nilai tetapi perbedaannya yield akan menghentikan
#fungsi dan menyimpan kondisi lokal agar bisa dilanjutkan tepat seperti saat dihentikan
def rev_string(mystr):
    length = len(mystr)
    
    #range(start,stop,step)
    for i in range(length - 1,-1,-1):
        yield mystr[i]

for char in rev_string(mystr="Hallo semua"):
    print(char)

colors = ["red","black","green","blue"]

def myfunction():
    for i in range(len(colors) -1,-1,-1):
        yield colors[i]

for color in myfunction():
    print(color)
