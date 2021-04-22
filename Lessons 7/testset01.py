#tipe data set disimbolkan dengan menggunakan {}
#di dalam tipe data set, data tidak terurut dan
#data yang sama akan dihilangkan nilainya yang lain
basket = {"apple","orange","apple","pear","orange","banana"}
print(basket)
print("orange" in basket)

print("crabgrass" in basket)

a = set ("abracadabra")
b = set ("alacazam")
print(a)
print(b)
print(a - b) #huruf yg ada di a,tetapi tidak di b
print(a | b) #huruf yang ada di a dan b , ditampilkan
print(a & b) #huruf yang ada di a dan b
print(a ^ b) #huruf yang ada di a dan b tetapi tidak ada di keduany
a = {x for x in "abracadabra" if x not in "abc"}
print(a)